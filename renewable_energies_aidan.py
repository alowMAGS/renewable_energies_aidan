# Make an introduction to find out information about the user
def check_name(question, error):
    run = True
    while run:
        # Ask the user for their name
        name = input(question).capitalize()
        print()
        # Output the user's name and ask if it is correct
        correct_name = input("Your name is {}. Is that correct? (Y/N) "
                             .format(name)).capitalize()
        print()
        # If the user inputs yes, output  their name
        if correct_name == 'Y':
            run = False
        # If the user inputs no, re-print the question
        elif correct_name == 'N':
            run = True
        # If the user doesn't input yes or no, output an error
        else:
            print(error)
            print()
    if not run:
        print("Hello", name)
    elif run:
        print(question)


print()
check_name("What is your name? ",
           "Please enter with 'Y' for yes or 'N' for no.")


def extra_info():
    while True:
        try:
            # Create an empty list to store user's age and city
            city_and_age = []
            # Ask the user for their city
            print()
            city = str(input("What city do you live in? ")).capitalize()
            # Add the inputted city into the empty list
            city_and_age.append(city)
            # Ask the user for their age
            print()
            age = int(input("What is your age? "))
            # Add the inputted age into the empty list
            city_and_age.append(age)
            # Print the user's city and age and check if it is correct
            print()
            correct_info = input("Is your city {} and is your age {}? (Y/N) ".format(city_and_age[0], city_and_age[1])).capitalize()
            if correct_info == 'Y':
                break
            elif correct_info == 'N':
                continue
        except ValueError:
            print()
            print("Please input a numerical variable")


extra_info()


def print_instructions(order):
    run = True
    while run:
        # Ask the user if they want to print the instructions
        print()
        help_needed = input(order).capitalize()
        # If the user inputs 'H', print the instructions
        if help_needed == 'H':
            run = False
            print()
            print("You chose to print instructions.")
            print()
            print("""*** Instructions ***
- You will be asked a series of questions with multiple choice answers.
- Please answer the as accurately as possible. If you are unsure of an answer,
  make a suitable guess.
- For every question, you will get a number of points depending on your answer.
- Once you have finished, your total will be calculated.
- Based on your results, you will be told if you are recommended to use more
  renewable energies or not.""")
            print()
        # If the user presses enter, continue the program
        elif help_needed == '':
            run = False
            print()
            print("You chose to continue.")
            print()

        # If the user doesn't input 'H' or the 'enter' key, print an error
        else:
            run = True
            print()
            print("Please enter with 'H' or press the 'enter' key")


print_instructions('''Enter 'H' if you would like to read the instructions
for this code. Press the 'enter' key if you would not
like to read the instructions. ''')

# ---------- Main ------------
# set user's points as 0 prior to the questions
points = 0
# ask the user the 1st question
question_1 = input("""1) How often do you eat meat or dairy?
A) Never
B) Once a month
C) Once a week
D) A few times a week
E) Every day
F) Every meal


""").capitalize()
# depending on the input, add points to the end user's total points
if question_1 == "A":
    points += 1

elif question_1 == "B":
    points += 2

elif question_1 == "C":
    points += 3

elif question_1 == "D":
    points += 4

elif question_1 == "E":
    points += 5

else:
    points += 6
# ask the user the 2nd question
question_2 = input("""2) How much of the food you eat is processed, packaged, or imported?
A) Most
B) Three quarters
C) Half
D) One quarter
E) Hardly any


""").capitalize()
# depending on the input, add points to the end user's total points
if question_2 == "A":
    points += 5

elif question_2 == "B":
    points += 4

elif question_2 == "C":
    points += 3

elif question_2 == "D":
    points += 2

else:
    points += 1
# ask the user the 3rd question
question_3 = input("""3) Do you have electricity in your home?
A) No
B) Yes
C) Green electricity


""").capitalize()
# depending on the input, add points to the end user's total points
if question_3 == "A":
    points += 0

elif question_3 == "B":
    points += 8

else:
    points += 4
# ask the user the 4th question
question_4 = input("""4) How much waste do you produce compared to other people where you live?
A) Much less
B) About the same
C) Much more


""").capitalize()
# depending on the input, add points to the end user's total points
if question_4 == "A":
    points += 3

elif question_4 == "B":
    points += 10

else:
    points += 30
# ask the user the 5th question
question_5 = input("""5) How many people live in your house?
A) 1
B) 2
C) 3
D) 4
E) 5


""").capitalize()
# depending on the input, add points to the end user's total points
if question_5 == "A":
    points += 50

elif question_5 == "B":
    points += 25

elif question_5 == "C":
    points += 6

elif question_5 == "D":
    points += 4

else:
    points += 2
# ask the user the 6th question
question_6 = input("""6) What kind of house do you live in?
A) Detached house
B) Semi-detached house
C) Apartment block
D) Green-design house


""").capitalize()
# depending on the input, add points to the end user's total points
if question_6 == "A":
    points += 10

elif question_6 == "B":
    points += 5

elif question_6 == "C":
    points += 4

else:
    points += 0
# ask the user the 7th question
question_7 = input("""7) How often do you travel on public transport?
A) Every day
B) Most days
C) Once or twice a week
D) Occasionally
E) Never


""").capitalize()
# depending on the input, add points to the end user's total points
if question_7 == "A":
    points += 20

elif question_7 == "B":
    points += 10

elif question_7 == "C":
    points += 6

elif question_7 == "D":
    points += 3

else:
    points += 0
# ask the user the 8th question
question_8 = input("""8) How often do you travel by car?
A) Every day
B) Most days
C) Once or twice a week
D) Occasionally
E) Never


""").capitalize()
# depending on the input, add points to the end user's total points
if question_8 == "A":
    points += 80

elif question_8 == "B":
    points += 40

elif question_8 == "C":
    points += 20

elif question_8 == "D":
    points += 10

else:
    points += 0
# ask the user the 9th question
question_9 = input("""9) How often do you cycle, walk, or get around using some
other means of self-generated power?
A) Most of the time
B) Sometimes
C) Never


""").capitalize()
# depending on the input, add points to the end user's total points
if question_9 == "A":
    points += 0

elif question_9 == "B":
    points += 2

else:
    points += 4
# ask the user the 10th question
question_10 = input("""10) How many hours have you spent flying this year?
A) 100 or more
B) 25
C) 10
D) 3
E) 0

""").capitalize()
# depending on the input, add points to the end user's total points
if question_10 == "A":
    points += 60

elif question_10 == "B":
    points += 30

elif question_10 == "C":
    points += 10

elif question_10 == "D":
    points += 5

else:
    points += 0

print("You have {} points".format(points))

if points <= 20:
    print()
    print("Green is your favourite colour - keep up the good work!")

elif points <= 100:
    print()
    print("Your efforts are appreciated!")

elif points <= 200:
    print()
    print("Room for improvement.")
    print()
    print("It is recommended that you use more renewable energies to help"
          "reduce your carbon emission.")

else:
    print()
    print("Look for better ways to become friends with Mother Nature!")
    print()
    print("It is recommended that you use more renewable energies to help"
          "reduce your carbon emission.")
