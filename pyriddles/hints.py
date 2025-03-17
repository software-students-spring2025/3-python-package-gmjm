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

