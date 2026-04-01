# 🎯 Requirements:
# Secret number = 7
# User keeps guessing
# If correct → "Correct!" and stop
# If wrong → "Try again"

secret_number = 7 

#while loop
while True:
        guess_number = int(input("Guess number: "))

        if guess_number == secret_number:
            print("You guess correct!")
            break
        else:
            print("Try again")
