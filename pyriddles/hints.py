# this is the main file for the four methods
from pyriddles.config import load_settings, RIDDLES
import random
import re
from morse3 import Morse
import pronouncing
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import logging

logging.basicConfig(filename="error.log", level=logging.ERROR)

lemmatizer = WordNetLemmatizer()

settings = load_settings()

riddles = {
    1: {
        "riddle": "What has keys but can't open locks?",
        "solution": "A piano",
        "hints": [
            "It's a musical instrument.",
            "Some of my keys are white, others black.",
            "I form melodies, not unlock doors.",
            "My keys are pressed, not turned."
        ]
    },
    2: {
        "riddle": "The more you take, the more you leave behind. What am I?",
        "solution": "Footsteps",
        "hints": [
            "They are momentarily visible in the sand",
            "The size of what you leave will change throughout your life"
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
        "hints": [
            "Sometimes a wave, sometimes a particle",
            "An easy way to brighten any day",
        ] 
    },
}




def random_hint(solution, hints_list):

    function_list = [ prewritten_hint, wordlength_hint, firstletters_hint, revealrandom_hint, wordscramble_hint, revealvowels_hint, 
                     soundsalad_hint, binary_hint, morse_hint, synonymsalad_hint ]
    
    attempts = 0
    max_attempts = 10  #prevent inf loops

    while attempts < max_attempts:
        chosen_func = random.choice(function_list)
        try:
            if chosen_func == prewritten_hint:
                hint = chosen_func(hints_list)
            else:
                hint = chosen_func(answer)

            # if the hint is same as answer- try again
            if hint == answer:
                logging.error(f"Generated hint is the same as the answer. Retrying...")
                attempts += 1
                continue

            return hint
        except Exception as e:
            logging.error(f"Error with {chosen_func.__name__}: {e}. Retrying...") #retry if any errors occur in other funcs
        
        attempts += 1

    return "Sorry, no valid hints available for this riddle."

def prewritten_hint(hints_list):
    """
    A function to randomly pick a prewritten hint from the riddles' dict.
    """
    if hints_list == []:
        raise ValueError("No hints are avaiable for this type. Please try another hint type.")
    return random.choice(hints_list)

def wordlength_hint(answer):
    """
    A function to generate a hint that displays the number of letters in the answer phrase.
    Ex. "The answer is n letters long."
    """
    wordlength = len(answer.replace(" ", ""))
    return "The answer is "+str(wordlength)+" letters long."

def firstletters_hint(answer):
    """
    A function to generate a hint that displays the first letter for every word of the answer phrase.
    Ex. "The first letter(s) of the answer is: F."
    """
    words = answer.split()
    firstletters = [word[0] for word in words if word]

    return 'The first letter(s) of the answer is: ' + ', '.join(firstletters)

def revealrandom_hint(answer):
    """
    A function to generate a hint that reveals random letters of the answer phrase.
    Ex. "Here are some letters revealed: _oo_st_p_"
    """
    words = answer.split()

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

    return "Here are some letters revealed: " + ' '.join(words)

def wordscramble_hint(answer):
    """
    A function to generate a hint that scrambles the letters of the answer phrase.
    Ex. "Here are the letters scrambled: otosFpse"
    """
    words = answer.split()
    for i, word in enumerate(words):
        tempchars = list(word)
        shuffled_word = word
        while shuffled_word == word: # shuffle until word is actually scrambled
            if len(word) == 1:
                break
            random.shuffle(tempchars) 
            shuffled_word = ''.join(tempchars)
        words[i] = shuffled_word # update word at same index
    return "Here are the letters scrambled: " + ' '.join(words)

def revealvowels_hint(answer):
    """
    A function to generate a hint that reveals all the vowels of the answer phrase.
    Ex. "Here are the vowels revealed: _oo___e__"
    """
    return "Here are the vowels revealed: "+ re.sub(r'[^aeiouAEIOU\s]', '_', answer) # regex replace all except vowels with "_"

def soundsalad_hint(answer):
    """
    A function to generate a hint that generates a rhyming word for each word in the answer phrase.
    Ex. "The answer sounds like: Quadriceps"
    """
    soundsalad = []
    for word in answer.split():
        rhymes = pronouncing.rhymes(word)
        if len(rhymes) > 0: #if rhymes exist
            soundsalad.append(random.choice(rhymes))
        else: # if no rhymes
            soundsalad.append(word) # append word as is
    return "The answer sounds like: " + ' '.join(soundsalad)

def binary_hint(answer):
    """
    A function to generate a hint that generates the answer phrase in binary code.
    Ex. "Here is the answer in binary code: 01000110 01101111 01101111 01110100 01110000 01110010 01101001 01101110 01110100 01110011"
    """
    return "Here is the answer in binary code: " + ' '.join(format(ord(_), '08b') for _ in answer)

def morse_hint(answer):
    """
    A function to generate a hint that generates the answer phrase in binary code.
    Ex. "Here is the answer in morse code: ..-. --- --- - .--. .-. .. -. - ..."
    """
    return "Here is the answer in morse code: "+ Morse(answer).stringToMorse()

def synonymsalad_hint(answer):
    """
    A function to generate a hint that generates a synonym for each word in the answer phrase.
    Ex. "Here's a synonym swap to guide you: Hoofprints"
    """
    synonymsalad = []
    for word in answer.split():
        lemma = lemmatizer.lemmatize(word)
        synsets = wordnet.synsets(lemma)
        if synsets:
            synonym_words = [lemma.name() for syn in synsets for lemma in syn.lemmas()]
            synonymsalad.append(random.choice(synonym_words))
        else:
            synonymsalad.append("[?]")
    return "Here's a synonym swap to guide you: " + ' '.join(synonymsalad)

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
    answer = riddle_id.get("answer")

    hint_func = HINT_TYPE_OPTIONS.get(str(hint_type))

    if hint_type == "prewritten_hint":
        result = hint_func(hints_list)
    elif hint_type in ("auto", "random_hint"):
        result = hint_func(answer, hints_list)
    else:
        result = hint_func(answer)
    
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

# get_hint(riddles.get(4), "soundsalad_hint")
#get_hints(riddles.get(4), "auto")