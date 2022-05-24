def main():
    password = get_password()
    for i in range(len(password)):
        print('*',end='')


def get_password():
    passWord = input("Enter the password: ")
    return passWord


main()