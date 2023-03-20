password = input('Enter password: ')
while len(password) < 5:
    print('Minimum password length is 5')
    password = input('Enter password: ')
print(len(password) * '*')
