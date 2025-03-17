# this will be the file for the hints function
import pyriddles as pr
from pyriddles.config import load_settings
import random
import re
from morse3 import Morse
import pronouncing
import emoji
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import warnings

lemmatizer = WordNetLemmatizer()

settings = load_settings()

#TODO: logic for getting/parsing riddles whether by ID or otherwise, for now will use fake data

riddles = {
    1: {
        "riddle": "What has keys but can't open locks?",
        "solution": "A piano",
        "hints": [
            "It's a musical instrument.",
            "It plays melodies, not unlocks doors.",
            "You press my keys to make sound."
        ]
    },
    2: {
        "riddle": "The more you take, the more you leave behind. What am I?",
        "solution": "Footsteps",
        "hints": [
            "Think about movement and leaving a trail."
        ] 
    },
    3: {
        "riddle": "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?",
        "solution": "A map",
        "hints": [
            "It's something you use to navigate.",
            "You might fold me up when traveling."
        ]
    },
    4: {
        "riddle": "What comes once in a minute, twice in a moment, but never in a thousand years?",
        "solution": "The letter M",
        # no hints field
    },
    5: {
        "riddle": "What can fill a room but takes up no space?",
        "solution": "Light",
        "hints": [] #empty list
    }
}


def random_hint(solution, hints_list):

    function_list = [ prewritten_hint, wordlength_hint, firstletters_hint, revealrandom_hint, wordscramble_hint, revealvowels_hint, 
                     soundsalad_hint, emoji_hint, binary_hint, morse_hint, synonymsalad_hint ]
    
    # remove any disabled types
    # disabled_hint_types = settings.get("disabled_hint_types")
    disabled_hint_types = []
    for func in disabled_hint_types:
        function_list.remove(func)

    chosen_func = random.choice(function_list)
    print("ima finna use "+ str(chosen_func))

    if chosen_func == prewritten_hint:
        chosen_func(hints_list)
    else:
        chosen_func(solution)

    # result = chosen_func(solution)
    # if result == -1
    # or catch any errors
    # try a diff random func
    return 0

def prewritten_hint(hints_list):
    """
    A function to randomly pick a prewritten hint from the riddles' dict.
    """
    if hints_list == []:
        # raise ValueError("No hints are avaiable for this type. Please try another hint type.")
        warnings.warn("No more hints are avaiable for this type. Please try another hint type.", UserWarning)
        return None
    return print(random.choice(hints_list))


#TODO: after testing, phase out print statements to actual return values

def wordlength_hint(solution):
    """
    A function to generate a hint that displays the number of letters in the solution phrase.
    Ex. "The solution is n letters long."
    """
    wordlength = len(solution.replace(" ", ""))
    return print("The solution is "+str(wordlength)+" letters long.")

def firstletters_hint(solution):
    """
    A function to generate a hint that displays the first letter for every word of the solution phrase.
    Ex. "The first letter(s) of the solution is: F."
    """
    words = solution.split()
    firstletters = [word[0] for word in words if word]

    return print('The first letter(s) of the solution is: ' + ', '.join(firstletters))

def revealrandom_hint(solution):
    """
    A function to generate a hint that reveals random letters of the solution phrase.
    Ex. "Here are some letters revealed: _oo_st_p_"
    """
    words = solution.split()

    for i, word in enumerate(words):
        tempchars = list(word)

        limit = int(len(word)/2) 

        # generate n random indexes btwn 0 and wordlen, n is the limit
        rand_indexes = [ random.randint(0,(len(word)-1)) for _ in range(limit)]

        # update chars in tempwords list at the random indexes to be "_"
        for x in rand_indexes:
            tempchars[x] = "_"

        word = ''.join(tempchars) # rejoin chars to be a word
        words[i] = word # update word at same index

    return print("Here are some letters revealed: " + ' '.join(words))

def wordscramble_hint(solution):
    """
    A function to generate a hint that scrambles the letters of the solution phrase.
    Ex. "Here are the letters scrambled: otosFpse"
    """
    words = solution.split()
    for i, word in enumerate(words):
        tempchars = list(word)
        shuffled_word = word
        while shuffled_word == word: # shuffle until word is actually scrambled
            if len(word) == 1:
                break
            random.shuffle(tempchars) 
            shuffled_word = ''.join(tempchars)
        words[i] = shuffled_word # update word at same index
    return print("Here are the letters scrambled: " + ' '.join(words))

def revealvowels_hint(solution):
    """
    A function to generate a hint that reveals all the vowels of the solution phrase.
    Ex. "Here are the vowels revealed: _oo___e__"
    """
    return print ("Here are the vowels revealed: "+ re.sub(r'[^aeiouAEIOU\s]', '_', solution)) # regex replace all except vowels with "_"

def soundsalad_hint(solution):
    """
    A function to generate a hint that generates a rhyming word for each word in the solution phrase.
    Ex. "The solution sounds like: Quadriceps"
    """
    soundsalad = []
    for word in solution.split():
        rhymes = pronouncing.rhymes(word)
        if len(rhymes) > 0: #if rhymes exist
            soundsalad.append(random.choice(rhymes))
        else: # if no rhymes
            soundsalad.append(word) # append word as is
    return print("The solution sounds like: " + ' '.join(soundsalad))

def emoji_hint(solution):
    """
    A function to generate a hint that generates an emoji for every word in the solution phrase.
    Ex. "Here's the solution in emojis: 👣"
    """
    
    return 0

def binary_hint(solution):
    """
    A function to generate a hint that generates the solution phrase in binary code.
    Ex. "Here is the solution in binary code: 01000110 01101111 01101111 01110100 01110000 01110010 01101001 01101110 01110100 01110011"
    """
    return print("Here is the solution in binary code: " + ' '.join(format(ord(_), '08b') for _ in solution))

def morse_hint(solution):
    """
    A function to generate a hint that generates the solution phrase in binary code.
    Ex. "Here is the solution in morse code: ..-. --- --- - .--. .-. .. -. - ..."
    """
    return print("Here is the solution in morse code: "+ Morse(solution).stringToMorse())

def synonymsalad_hint(solution):
    """
    A function to generate a hint that generates a synonym for each word in the solution phrase.
    Ex. "Here's a synonym swap to guide you: Hoofprints"
    """
    synonymsalad = []
    for word in solution.split():
        lemma = lemmatizer.lemmatize(word)
        synsets = wordnet.synsets(lemma)
        if synsets:
            synonym_words = [lemma.name() for syn in synsets for lemma in syn.lemmas()]
            synonymsalad.append(random.choice(synonym_words))
        else:
            synonymsalad.append("[?]")
    return print("Here's a synonym swap to guide you: " + ' '.join(synonymsalad))

HINT_TYPE_OPTIONS = {
    "auto": random_hint,
    "random_hint": random_hint,
    "prewritten_hint": prewritten_hint,
    "wordlength_hint": wordlength_hint,
    "firstletters_hint": firstletters_hint,
    "revealrandom_hint": revealrandom_hint,
    "wordscramble_hint": wordscramble_hint,
    "revealvowels_hint": revealvowels_hint,
    "soundsalad_hint": soundsalad_hint,
    "emoji_hint": emoji_hint,
    "binary_hint": binary_hint,
    "morse_hint": morse_hint,
    "synonymsalad_hint": synonymsalad_hint
}

def get_hint(riddle_id, hint_type="auto"):
    """
    Generates a single hint for a riddle.
    """

    if "hints" not in riddle_id:
        riddle_id.update({"hints":[]})

    hints_list = riddle_id.get("hints")
    print(hints_list)
    solution = riddle_id.get("solution")

    hint_func = HINT_TYPE_OPTIONS.get(str(hint_type))

    # if chosen hint_type is disabled
    # disabled_hint_types = settings.get("disabled_hint_types")
    disabled_hint_types = []
    if hint_func in disabled_hint_types:
        raise ValueError("This hint type is disabled. Update your settings to enable it.")

    if hint_type == "prewritten_hint":
        result = hint_func(hints_list)
    elif hint_type == "auto" or "random_hint":
        result = hint_func(solution, hints_list)
    else:
        result = hint_func(solution)
    
    if result == -1: 
        return "Sorry, no more hints are avaiable for this type. Please try another hint type."
    else:
        pass


    return result


def get_hints(riddle_id, hint_type="auto", limit=10):
    """
    Generates a list of hints, up to specified limit. The limit is 10 by default.
    """
    hints_list = [get_hint(riddle_id, hint_type) for _ in range(limit)]
    return hints_list

get_hint(riddles.get(1))