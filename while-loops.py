countdown_number = 10

print("Initiating Countdown Sequence...")
print("Lift Off Will Commence In...")

while countdown_number >= 0:
    print(f"{countdown_number} seconds...")
    countdown_number -= 1

print("And We Have Lift Off!")

#Runnable Example
play_game = True

while play_game:
    continue_playing = input("Would you like to continue playing the game? y/n ")
    
    if continue_playing.lower() == "y":
        print("You have decided to continue playing the game.")
    elif continue_playing.lower() == "n":
        print("Now closing the game...")
        play_game = False
    else:
        print("That is not a valid option. Please try again.")

print("Thanks for playing")

#Challenge
number = 0
while number <=9:
    print(number)
    number += 1