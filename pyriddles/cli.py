# this file will handle/parse command line interaction for our package

#TODO: write functions for a CLI parser that allows users to interact with our package via using commands like
#      'pyriddles --help' or 'pyriddles --difficulty hard' or etc.

from pyriddles.config import RIDDLES

def get_answer(riddle_id):
    riddle = RIDDLES.get(riddle_id)
    if riddle:
        return riddle["answer"]
    return "Riddle not found."
