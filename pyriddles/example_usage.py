from pyriddles import list_difficulties, get_riddle_by_difficulty, arbitrary_riddle, get_answer, get_hint, get_hints, RIDDLES

# Demonstrate arbitrary_riddle
riddle_id = arbitrary_riddle()
print(f"Random riddle ID: {riddle_id}")

#Demonstrate get_answer
answer = get_answer(riddle_id)
print(f"The answer to riddle {riddle_id} is: {answer}")

#Demonstrate list_difficulties
print(list_difficulties())

# Demonstrate proper usage of get_riddle_by_difficulty
print(get_riddle_by_difficulty("easy"))

# Demonstrate improper usage of get_riddle_by_difficulty
print(get_riddle_by_difficulty("extra hard"))

#Demonstrate get_hint and get_hints
riddle_id = RIDDLES.get(4)

if riddle_id:
    print("Riddle:", riddle_id.get("question", "No question provided"))

    #Example usage of get_hint

    hint = get_hint(riddle_id, "soundsalad_hint")
    print("Generated hint (soundsalad_hint):", hint)

    hint_auto = get_hint(riddle_id, "auto")
    print("Generated hint (auto):", hint_auto)

    #Example usage of get_hints

    hints_list = get_hints(riddle_id, "auto", limit=5)
    print("Generated list of hints (auto):", hints_list)

else: 
  print("Riddle not found in dataset.")