def days_to_unit(num_of_days):
        return f"{num_of_days} days are {num_of_days * 24} hours"



def validate_and_execute():

    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_unit(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered 0, please enter a number")
        else:
            print("You entered a negative number, no coversion of you")

    except ValueError:
        print("I can't covert this")


for i in range(10):
    user_input = input("Hey, user ! enter a number of days and i wll convert it in hours! \n")
    validate_and_execute()



