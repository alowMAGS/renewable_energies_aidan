# Make an introduction to find out information about the user
def check_name(question, error):
    run = True
    while run:
        # Ask the user for their name
        name = input(question)
        print()
        # Output the user's name and ask if it is correct
        correct_name = input("Your name is {}. Is that correct? (Y/N) ".format(name)).capitalize()
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
check_name("What is your name? ", "Please enter with 'Y' for yes or 'N' for no.")




