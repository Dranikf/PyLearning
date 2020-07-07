names = ['bob' , 'alice' , 'mike' , 'admin', 'killa']

newUsers = ['BOB' , 'Carl' , 'killa']

for name in newUsers:
    if name.lower() in names:
        print(name + ' is already used. Please choose new login')
    else:
        print('welcome ' + name);
        names.append(name.lower());

if not names:
    print('no users');
    exit()

for name in names:
    if name == 'admin':
        print('hello admin, would you like to see report?');
    else:
        print('hello ' + name + ' nice to see you again!');
