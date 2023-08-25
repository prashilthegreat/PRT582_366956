"""import random and regular expressions"""
import random
import re

NUM = 0



def number_generator():
    """This function generates the 4 digit number."""
    return random.randint(1000, 9999)


def get_user_input():
    """Function to get and check user input"""
    count = 0
    print(
        "Welcome. Try and guess a 4 digit number, the computer gives you x and circle."
    )
    print(
        "Circle means the digit is the right place.X means the digit is not in the right place."
    )
    while True:
        user_input = input("Enter a 4 digit number to guess or press enter to quit! ")
        count += 1
        if check_if_user_is_quitting(user_input):
            output_message = "You lose. The number was " + str(NUM)
            print(output_message)

            break
        if not check_if_valid_input(user_input):
            output_message = "Invalid input. Enter only 4 digit numbers"
            print(output_message)
            continue
        output_message = "Valid"
        if check_if_correct_guess(user_input)[0]:
            output_message = (
                "Congratulations you won! You took " + str(count) + " attempts."
            )
            print(output_message)
            new_input = input("Do you want to play again? Y/N ")
            if new_input.lower() == "y":
                main()
            break

        continue


def check_if_user_is_quitting(input_string):
    """This function checks if the user is quitting"""
    return input_string == ""


def check_if_valid_input(input_string):
    """This functions checks if the entered input is valid for our game"""
    if re.search("[a-z]", input_string.lower()):
        return False
    try:
        integer_guess = int(input_string)
        if (
            integer_guess < 1000 or integer_guess > 9999
        ):  # if the input is 3 digit or 5+ digits
            return False
        return True
    except ValueError:
        return False


def check_if_correct_guess(input_string):
    """This function provides the hints for the guesses."""
    num_list = []
    num_list2 = []
    hint_list = ["_", "_", "_", "_"]
    manipulating_random_number = NUM
    mainpulating_user_input = int(input_string)

    for i in range(0, 4):
        #splitting the 4 digit number into single digits by using remainders after dividig by 10.
        remainder1 = manipulating_random_number % 10
        remainder2 = mainpulating_user_input % 10
        manipulating_random_number = manipulating_random_number // 10
        mainpulating_user_input = mainpulating_user_input // 10
        num_list.append(remainder1)
        num_list2.append(remainder2)
    num_list.reverse() #reversing to get the actual number again
    num_list2.reverse()
    for i,element in enumerate(num_list2):
        element = num_list2[i]
        if element in num_list:
            if num_list[i] == element:
                hint_list[i] = num_list2[i] = "circle"
            else:
                hint_list[i] = num_list2[i] = "x"

    print("HINTS: ", hint_list)

    if hint_list.count("circle") == 4:
        return [True, hint_list]
    return [False, hint_list]


def main(is_from_test=False):
    """This is the main function"""
    if (
        not is_from_test
    ):  # in unit test im giving hard coded inputs, different test cases
        get_user_input()


if __name__ == "__main__":
    NUM = number_generator()
    main()
else:
    NUM = 5396
    main(True)
