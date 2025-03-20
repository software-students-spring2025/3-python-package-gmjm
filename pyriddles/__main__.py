import pyriddles.hints as hints

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