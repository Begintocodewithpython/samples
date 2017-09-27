# EG5-08 Greeter with password

name = input('Enter your name: ')

if name.upper() == 'ROB':
    password = input('Enter the password: ')
    if password == 'secret':
        print('Hello, Oh great one')
    else:
        print('Begone. Imposter')
