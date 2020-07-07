pizzas = ['four seasons' , 'margarita', 'peperoni', 'hueoni' , 'pizdaoni', 'gavnosroni'] 

print('my favorite pizzas is:')
for p in pizzas:
    print('I like ' + p + ' pizza');

print('I really love pizza!');

print('\nFirst three items are:')
[print(value) for value in pizzas[:3]]

print('\nMidle three items are:')
[print(value) for value in pizzas[2:5]]

print('\nLast three items are:')
[print(value) for value in pizzas[3:6]]

friends_pizzas = pizzas[:];
pizzas.append('herlione');

friends_pizzas.append('friend piazza');

print('\nmy pizzas');
[print(value) for value in pizzas]
print('\nfriend pizzas');
[print(value) for value in friends_pizzas]
