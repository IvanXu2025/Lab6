#Ivan Xu
def menu():
    def encoder(password):
        encoded = ''
        for x in password:
            new_digit = (int(x)+3)
            encoded += str(new_digit)
        return encoded


    password = ''
    encoded_password = ''


    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')

        choice = input('Please enter an option: ')

        if choice == '1':
            password = input('Please enter your password to encode: ')
            new_password = encoder(password)
            print('Your password has been encoded and stored!')
        elif choice == '2':
            print(f"The encoded password is {encoded_password}, and the original password is {password}")
        elif choice == '3':
            exit()

menu()
