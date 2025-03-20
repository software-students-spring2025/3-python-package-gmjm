from .__main__ import list_difficulties, get_riddle_by_difficulty

print(list_difficulties())

# valid difficulty
print(get_riddle_by_difficulty("easy"))

# invalid difficulty
print(get_riddle_by_difficulty("extra hard"))