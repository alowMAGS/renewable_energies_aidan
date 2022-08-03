# Ask the user if they want to print the instructions
help_needed = input("Enter 'H' if you would like to read the instructions for this code. ").capitalize()
# If the user inputs 'H', print the instructions
if help_needed == 'H':
    print()
    print("Instructions go here")
# If the user doesn't input 'H', continue the program
else:
    print("continue program")