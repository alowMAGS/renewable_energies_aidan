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
