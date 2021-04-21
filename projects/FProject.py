import random 
# Creates variables for random numbers 
odd_number = random.randint(1,10)
tries = 1
 # Asks for users input name & if they want to play the guessing game
name = input("Hello, What's your Name cutiepie ")
 
print("Hello", name+",", )
 
question = input("Would you Like To Guess a Number ? [Y/N] ")
 
if question == "n":
    print("oh..no problem")
 # Creates main game loop
if question == "y":
    print("Say A Number Between 1 & 10")
    guess = int(input("Make a Guess, I will be nice and give one hint;P : "))
    if guess > odd_number:
        print("Guess Lower than ", guess)
    if guess < odd_number:
        print("Guess Higher than ", guess)
   # Do while loop that continues to check for the correct answer
    while guess != odd_number:
        tries += 1
        guess = int(input("Try Again : ")) 
        if guess == odd_number:
            print("That's Right! winner! It Was", odd_number, "and it only", tries, "tries!")
