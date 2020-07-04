firends_names = ['sergey', 'nikita', 'nadya', 'andrey']

print(firends_names);
print(firends_names[0].title())
print(firends_names[1].title())
print(firends_names[2].title())
print(firends_names[3].title())


message = 'happy dirsday ';


print(message + firends_names[0].title())
print(message + firends_names[1].title())
print(message + firends_names[2].title())
print(message + firends_names[3].title())

firends_names.append('places for new friend')
print(firends_names)

firends_names.insert(0 , 'old friend')
print(firends_names)

del firends_names[1]
print(firends_names)

print(firends_names.pop(1))
print(firends_names)

firends_names.remove('andrey')
print(firends_names)
