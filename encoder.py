def encode(password):
    encoded = ''
    for x in password:
        new_digit= ((int(x)+3)%10)
        encoded += str(new_digit)
    return encoded
