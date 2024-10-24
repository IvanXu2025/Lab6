from encoder import encode
#from decoder import decode

start = ''
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
        start = input('Please enter your password to encode: ')
        encoded_password = encode(start)
        print('Your password has been encoded and stored!')
    elif choice == '2':
        #password = decode(new_password)
        print(f"The encoded password is {encoded_password}, and the original password is {password}")
    elif choice == '3':
        exit()