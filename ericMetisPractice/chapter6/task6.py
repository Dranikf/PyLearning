favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

people = ['jen' , 'sarah' , 'edward' , 'phil', 'fedor' , 'serhey'];

for men in people:
    if men in favorite_languages.keys():
        print('thank you ' + men);
    else:
        print(men + ' would you like to take part?')
