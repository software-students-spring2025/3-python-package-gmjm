from pyriddles.config import RIDDLES, DEFAULT_SETTINGS, DIFFICULTIES
import pyriddles.hints as hints
import random

def arbitrary_riddle():
    riddle_id = random.randint(1,10)
    return riddle_id

def get_answer(riddle_id):
    riddle = RIDDLES.get(riddle_id)
    if riddle:
        return riddle["answer"]
    return "Riddle not found."

def list_difficulties():

    if len(DIFFICULTIES) == 0:
        return "There are no levels of difficulty."
    
    output = "The available riddle difficulties are:\n"

    for difficulty in DIFFICULTIES:
        output += difficulty + "\n"

    return output

def get_riddle_by_difficulty(difficulty):

    # ensure difficulty exists
    if difficulty not in DIFFICULTIES:
        return "Not a valid difficulty."

    # create new dictionary with riddles from RIDDLES that have the same difficulty
    filtered_riddles = {key: value for key, value in RIDDLES.items() if value["difficulty"] == difficulty}

    # choose random riddle key and store the associated key-value pair
    random_riddle_key = random.choice(list(filtered_riddles.keys()))
    random_riddle = filtered_riddles[random_riddle_key]

    return "Here is a " + difficulty + " riddle!\n" + random_riddle["question"]