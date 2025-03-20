from pyriddles.config import RIDDLES, DEFAULT_SETTINGS, DIFFICULTIES
import pyriddles.hints as hints
import random


def get_riddle():
    riddle_id = 0
    while not (1 <= riddle_id <= 5):
        answer = input("Choose a number from 1-5 (inclusive): ")
        if answer.isdigit():
            riddle_id = int(answer)
            if 1 <= riddle_id <= 5:
                break
            else:
                print("Try again! That wasn't a number from 1-5!")
        else:
            print("That wasn't a number! Please enter a number!")
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

def main():
    riddles = hints.riddles
      
    riddle_id = get_riddle()  

    riddle_data = riddles[riddle_id]  
    print(f"Riddle {riddle_id}: {riddle_data['riddle']}")
    
    while True:
      user_answer = input("Your answer: ")

      if user_answer.lower() == riddle_data['solution'].lower():
          print("Correct!")
          break
      else:
          print("Incorrect. Here's a hint:")
          hints.get_hint(riddle_data)  
    

if __name__ == "__main__":
  main()