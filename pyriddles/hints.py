# this will be the file for the hints function

#TODO: logic for getting/parsing riddles whether by ID or otherwise, for now will use fake JSON data

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


def get_hint(riddle_id, hint_type):


    #TODO: get solution from ID and parse it (to string if needed)
    # solution = solution
    # call funcs like random_hint(solution)
    # for prewritten_hint, also get hintslist from ID
    hints_list = riddle_id.get("hints")

    # TODO: if hint_type = default / random_hint()
    #       handle if none of the random hints work- print "Sorry, no more hints are available for this riddle."

    #TODO: if specific hint_type = chosen_func
    # if in disabled_hint_types in config.py then print "No hints available. Enable this hint type in settings.json first."
    # if the hint type doesn't apply or runs out or wtv- print "Sorry, no hints are available. Please try another hint type."

    return 0

def random_hint(riddle_string):
    #TODO: randomly call one of the hint funcions, active ones only 
    # so if hint_func not in disabled_hint_types from config.py...

    # if the functions return -1, then try another random function - bc this will mean that hint type is not available for this riddle

    # maybe take difficulty param, and only call random hints belonging to set difficulty. or if not, then allow toggle of hard weird hints off
    return 0

def prewritten_hint(hints_list):
    #TODO: if hints is empty or doesn't exist

    #TODO: track previously outputted hints so that none is repeated

    # if no hints or it's all run out, then print sorry- no more prewritten hints

    return 0

#TODO: maybe: option to toggle hintdescriptions when the answer is printed vs just priting the hint straight up?

def wordlength_hint(riddle_string):
    """
    A function to generate a hint that displays the wordcount of the solution phrase.
    Ex. "The answer is n words long."
    """


    
    return 0

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