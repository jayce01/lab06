def encode(password):  #Creates encode for password by adding 3 to user input
    newPass = ''
    for x in password:
        num = int(x)
        if num == 9:
            num = 2
        elif num == 8:
            num = 1
        elif num == 7:
            num = 0
        else:
            num = num + 3
        newPass += str(num)
    return newPass


def menu():  #creates print menu
    print("""
    Menu
    -----------
    1. Encode
    2. Decode
    3. Quit
    """)


def decode(password):
    decoded_password = ""
    for char in password:
        num = int(char)
        num -= 3
        if num < 0:
            num += 10
        decoded_password += str(num)
    return decoded_password


def main():  #run program
    option = 0
    userPass = ''
    while option != 3:
        main()
        option = int(input("Please enter an option: "))
        if option == 1:
            userPass = input("Please enter a password to encode: ")
            print("Your password has been encoded and stored!")
            userPass = encode(userPass)
        if option == 2:
            print(f"The encoded password is {userPass} and the original password is " + decode(userPass))


if __name__ == '__main__':  #make code work
    main()
