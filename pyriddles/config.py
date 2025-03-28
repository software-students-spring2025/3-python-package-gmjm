# this file will store the default settings of our package

DEFAULT_SETTINGS = { # feel free to add, remove, adjust, etc. these as needed
    "difficulty": "medium",
    "hint_limit": 3,
    "disabled_hint_types":[]
}

DIFFICULTIES = ["easy", "medium", "hard"]

# TODO: write function to allow users to optionally create a 'settings.json' file in their app to override the default settings.
#      check first if a 'settings.json' exists and return those values,
#      otherwise return the DEFAULT_SETTINGS
#      - handle cases where settings.json has an error ex. incorrect format or key
def load_settings():
    return 0

# TODO: optionally, write function to restore user's current settings.json to the default settings (to be used in the cli args, ex. user types 'pyriddles resetsettings')
def reset_settings():
    return 0

# riddles dictionary
RIDDLES = {
    1: {
        "question": "I speak without a mouth and hear without ears. I have nobody, but I come alive with the wind. What am I?",
        "answer": "An echo",
        "difficulty": "medium",
        "hint": "Think about something that can be heard but not seen"
    },
    2: {
        "question": "I’m tall when I’m young, and I’m short when I’m old. What am I?",
        "answer": "A candle",
        "difficulty": "easy",
        "hint":"Think about something that changes shape over time"
    },
    3: {
        "question": "The more of this there is, the less you see. What is it?",
        "answer": "Darkness",
        "difficulty": "easy",
        "hint": "Think about something that affects your visibility"
    },
    4: {
        "question": "What can travel around the world while staying in the same corner?",
        "answer": "A stamp",
        "difficulty": "medium",
        "hint": "Think about something that can move around the world without actually moving on its own"
    },
    5: {
        "question": "I have cities, but no houses; mountains, but no trees; and water, but no fish. What am I?",
        "answer": "A map",
        "difficulty": "medium",
        "hint": "Think about something that represents a place or location"
    },
    6: {
        "question": "What is seen in the middle of March and April that can’t be seen at the beginning or end of either month?",
        "answer": "The letter 'R'",
        "difficulty": "hard",
        "hint": "Think about something that is visible in the middle of a word or phrase"
    },
    7: {
        "question": "You measure my life in hours and I serve you by expiring. I’m quick when I’m thin and slow when I’m fat. The wind is my enemy.",
        "answer": "A candle",
        "difficulty": "hard",
        "hint": "Think about something that has a limited lifespan and is affected by external factors"
    },
    8: {
        "question": "What has to be broken before you can use it?",
        "answer": "An egg",
        "difficulty": "easy", 
        "hint": "Think about something that needs to be opened, or CRACKED before it can be used"
    },
    9: {
        "question": "I have keys but no locks. I have space but no room. You can enter, but you can’t go outside. What am I?",
        "answer": "A keyboard",
        "difficulty": "medium",
        "hint": "Think about something that has keys or buttons but is not a physical lock"
    },
    10: {
        "question": "What disappears as soon as you say its name?",
        "answer": "Silence",
        "difficulty": "easy",
        "hint": "Think about something that is affected by sound or noise"
    }
}

