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
- Please answer the as accurately as possible. If you are unsure of an answer, make a suitable guess.
- For every question, you will get a number of points depending on your answer. 
- Once you have finished, your total will be calculated.
- Based on your results, you will be told if you are recommended to use more renewable energies or not.""")
            # If the user presses enter, continue the program
            elif help_needed == '':
                run = False
                print()
                print("You chose to continue.")
                print()
                print("continue program")


            # If the user doesn't input 'H' or the 'enter' key, print an error
            else:
                run = True
                print()
                print("Please enter with 'H' or press the 'enter' key")


print_instructions("Enter 'H' if you would like to read the instructions for this code. "
                   "Press the 'enter' key if you would not like to read the instructions. ")