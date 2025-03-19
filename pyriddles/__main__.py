from pyriddles.config import RIDDLES
import pyriddles.hints as hints


def get_riddle():
    riddle_id = 0
    while riddle_id < 1 or riddle_id > 5:
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


def main():
    riddles = hints.get_riddles()
      
    riddle_id = get_riddle()  

    riddle_data = riddles[riddle_id]  
    print(f"Riddle {riddle_id}: {riddle_data['riddle']}")
    
    user_answer = input("Your answer: ")

    if user_answer.lower() == riddle_data['solution'].lower():
        print("Correct!")
    else:
        print("Incorrect. Here's a hint:")
        hints.get_hint(riddle_data)  
    

    if __name__ == "__main__":
      main()