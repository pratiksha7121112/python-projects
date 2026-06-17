import random

attempt_easy = 10
attempt_medium = 7
attempt_hard = 5
high_score = 0
while True:

    print("Number Guessing Game")
    print("")
    print("Difficulty levels")
    print("")
    print("1. Easy")
    print("")
    print("2. Medium")
    print("")
    print("3. Hard")
    print("")
    print("4. Quit")
    print("")
    difficulty_choice = input("Choose a difficulty: ").lower()

    if difficulty_choice == "1":
     attempt_easy = 10
     easy = random.randint(1,50)
     while attempt_easy > 0:
        print("Choose a number between 1 to 50")
        print("You have",attempt_easy,"attempts")
        guess = int(input("Enter your guess: "))
        if guess < 1 or guess > 50:
               print("Please enter a number between 1 to 50")
               continue
        if guess == easy:
            score = attempt_easy 
            print("Your guess is correct!!")
            print("Your score:",score)
            if score > high_score: 
                high_score = score
                print("New high score!",high_score)
            else:
                print("High score:",high_score)
            break
        elif guess > easy:
            print("Too high!")
            attempt_easy -= 1
        elif guess < easy:
            print("Too low!")
            attempt_easy -= 1
     if attempt_easy == 0:
        print("Game over, the number was",easy)

    elif difficulty_choice == "2":
     attempt_medium = 7
     medium = random.randint(1,100)
     while attempt_medium > 0:
        print("Choose a number between 1 to 100")
        print("You have",attempt_medium,"attempts")
        guess = int(input("Enter your guess: "))
        if guess < 1 or guess > 100:
               print("Please enter a number between 1 to 100")
               continue
        if guess == medium:
            score = attempt_medium
            print("Your guess is correct!!")
            print("Your score:",score)
            if score > high_score:
                high_score = score
                print("New high score!",high_score)
            else:
                print("High score:",high_score)
            break
        elif guess > medium:
            print("Too high!")
            attempt_medium -= 1
        elif guess < medium:
            print("Too low!")
            attempt_medium -= 1
     if attempt_medium == 0:
        print("Game over, the number was",medium)

    elif difficulty_choice == "3":
     attempt_hard = 5
     hard = random.randint(1,200)
     while attempt_hard > 0:
        print("Choose a number between 1 to 200")
        print("You have",attempt_hard,"attempts")
        guess = int(input("Enter your guess: "))
        if guess < 1 or guess > 200:
               print("Please enter a number between 1 to 200")
               continue
        if guess == hard:
            score = attempt_hard 
            print("Your guess is correct!!")
            print("Your score:",score)
            if score > high_score: 
                high_score = score
                print("New high score!",high_score)
            else:
                print("High score:",high_score)
            break
        elif guess > hard:
            print("Too high!")
            attempt_hard -= 1
        elif guess < hard:
            print("Too low!")
            attempt_hard -= 1
     if attempt_hard == 0:
        print("Game over, the number was",hard)
    
    elif difficulty_choice == "4":
        break

    else:
       print("Invalid difficulty!")
       continue
    play_again = input("Play again? (Yes/No): ").lower()
    if play_again == "no":
       break
