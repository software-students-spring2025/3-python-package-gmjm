# this will be the file for the hints function
import pyriddles as pr
import random

settings = pr.load_settings()

#TODO: logic for getting/parsing riddles whether by ID or otherwise, for now will use fake data

riddles = {
    1: {
        "riddle": "What has keys but can't open locks?",
        "answer": "A piano",
        "hints": [
            "It's a musical instrument.",
            "It plays melodies, not unlocks doors.",
            "You press my keys to make sound."
        ]
    },
    2: {
        "riddle": "The more you take, the more you leave behind. What am I?",
        "answer": "Footsteps",
        "hints": [
            "Think about movement and leaving a trail."
        ] 
    },
    3: {
        "riddle": "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?",
        "answer": "A map",
        "hints": [
            "It's something you use to navigate.",
            "You might fold me up when traveling."
        ]
    },
    4: {
        "riddle": "What comes once in a minute, twice in a moment, but never in a thousand years?",
        "answer": "The letter M",
        # no hints field
    },
    5: {
        "riddle": "What can fill a room but takes up no space?",
        "answer": "Light",
        "hints": [] #empty list
    }
}


    # TODO: if a hint type runs out, the hint type func should return -1
    #       but for random_hint should return "Sorry, no more hints are available for this riddle."
    #       or maybe: decide if duplicate/repeated hint responses are ok bc then it'll nvr run out

def random_hint(riddle_string):
    #TODO: randomly call one of the hint funcions, active ones only 
    # so if hint_func not in disabled_hint_types from config.py...

    # if the functions return -1, then try another random function - bc this will mean that hint type is not available for this riddle

    # maybe take difficulty param, and only call random hints belonging to set difficulty. or if not, then allow toggle of hard weird hints off

    # TODO: handle if none of the random hints work- print "Sorry, no more hints are available for this riddle."
    # TODO: make it so where each hint can only be used once in a session, or set the ones that shouldn't be repeated
    return 0

def prewritten_hint(hints_list):
    """
    A function to randomly pick a prewritten hint from the riddles' dict.
    """
    if hints_list == []:
        return -1
    
    #TODO: track previously outputted hints so that none is repeated
    # if no hints or it's all run out, then print sorry- no more prewritten hints
    
    return random.choice(hints_list)


#TODO: maybe: option to toggle hintdescriptions when the answer is printed vs just priting the hint straight up?

def wordlength_hint(riddle_string):
    """
    A function to generate a hint that displays the number of letters in the solution phrase.
    Ex. "The answer is n letters long."
    """
    wordlength = len(riddle_string.replace(" ", ""))
    return print("The solution is "+str(wordlength)+" letters long.")

def firstletters_hint(riddle_string):
    """
    A function to generate a hint that displays the first letter for every word of the solution phrase.
    Ex. "The first letter(s) of the solution is: F."
    """
    return 0

def revealrandom_hint(riddle_string):
    """
    A function to generate a hint that reveals random letters of the solution phrase.
    Ex. "Here are some letters revealed: _oo_st_p_"
    """
    return 0

def wordscramble_hint(riddle_string):
    """
    A function to generate a hint that scrambles the letters of the solution phrase.
    Ex. "Here are the letters scrambled: otosFpse"
    """
    return 0

def revealvowels_hint(riddle_string):
    """
    A function to generate a hint that reveals all the vowels of the solution phrase.
    Ex. "Here are the vowels revealed: _oo___e__"
    """
    return 0

def soundsalad_hint(riddle_string):
    """
    A function to generate a hint that generates a rhyming word for each word in the solution phrase.
    Ex. "The answer sounds like: Quadriceps"
    """
    #TODO: exclude stopwords
    return 0

def emoji_hint(riddle_string):
    """
    A function to generate a hint that generates an emoji for every word in the solution phrase.
    Ex. "Here's the answer in emojis: 👣"
    """
    
    return 0

def binary_hint(riddle_string):
    """
    A function to generate a hint that generates the solution phrase in binary code.
    Ex. "Here is the answer in binary code: 01000110 01101111 01101111 01110100 01110000 01110010 01101001 01101110 01110100 01110011"
    """
    return 0

def morse_hint(riddle_string):
    """
    A function to generate a hint that generates the solution phrase in binary code.
    Ex. "Here is the answer in morse code: ..-. --- --- - .--. .-. .. -. - ..."
    """
    return 0

def synonymsalad_hint(riddle_string):
    """
    A function to generate a hint that generates a synonym for each word in the solution phrase.
    Ex. "Think of an answer similar to: Hoofprints"
    """
    return 0

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
    solution = riddle_id.get("answer")

    hint_func = HINT_TYPE_OPTIONS.get(str(hint_type))

    # if chosen hint_type is disabled
    disabled_hint_types = settings.get("disabled_hint_types")
    if hint_func in disabled_hint_types:
        print("Sorry, no hints are available. Please try another hint type.")
        return 1

    if hint_type == "prewritten_text":
        result = hint_func(hints_list)
    else:
        result = hint_func(solution)
    
    if result == -1: # only specific hint type funcs can return -1, random_hint has a diff handling
        return "Sorry, no more hints are avaiable for this type. Please try another hint type."
    else:
        pass

    # TODO: how to ensure a hint isn't printed twice

    return result

# cli wld b like user calles gethint() repeatedly until they're told there's no more 


def get_hints(riddle_id, hint_type="auto", limit=10):
    """
    Generates a list of hints, up to specified limit. The limit is 10 by default.
    """
    hints_list = [get_hint(riddle_id, hint_type) for _ in range(limit)]
    return hints_list