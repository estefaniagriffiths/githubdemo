# Estefania Griffiths


# encodes password by shifting each digit up 3 then storing it in a new variable
# the function takes the parameter "password" as the user input in the main function
def encode(password):
    encoded_password = ""  # empty string which will hold the new encoded password

    for digit in password:  # iterates over each digit in the password
        # adds 3 to the current digit then appends it to the end of the encoded password
        encoded_num = (int(digit) + 3) % 10  # convert to integer for addition, then modulus to eliminate negatives
        encoded_num = str(encoded_num)  # convert back to string
        encoded_password += encoded_num

    return encoded_password


# decodes the password by reversing what the encoded function does
# takes the encoded password as a parameter and returns the original password
def decode(encoded_password):
    decoded_password = ""  # empty string which will hold the decoded password

    for digit in encoded_password:  # iterates over each digit in the encoded password
        # subtracts 3 to the current digit then appends it to the end of the decoded password
        decoded_num = (int(digit) - 3) % 10  # convert to integer for subtraction, then modulus to eliminate negatives
        decoded_num = str(decoded_num)  # convert back to string
        decoded_password += decoded_num

    return decoded_password


# displays the menu of options for the user to choose from
def display_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")


# main function
def main():
    encoded_password = None

    # loops until user inputs 3
    while True:
        display_menu()
        user_option = int(input("Please enter an option: "))

        # if user enters 1, prompts them to enter a password to be decoded
        if user_option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")

        # if user enters 2, decodes the encoded password then displays both the encoded and original passwords
        elif user_option == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}\n")

        # if user enters 3, end the program
        elif user_option == 3:
            break


if __name__ == "__main__":
    main()
