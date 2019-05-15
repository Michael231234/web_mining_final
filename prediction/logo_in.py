tag = True
count = 1
while tag:
    if count > 3:
       break
    name = input('name>>: ')
    passwd = input('password>>: ')
    if name == 'seven' and passwd == '123':
        print('login successful!')
        break
    else:
        print('login failed')
        count += 11