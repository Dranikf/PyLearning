import json;


names_numbers = {};


try:
    with open('numbers.txt') as f_obj:
        names_numbers = json.load(f_obj);
except FileNotFoundError:
    names_numbers = {};

prin('already have info');
for name , number in names_numbers.items():
    print(name + ' : ' + number);

while True:

    name = input('user name: ');
    number = input('what the best number: ');
    
    names_numbers[name] = number;
    
    signal = input('q for quit: ')
    if(signal == 'q'):
        break;


with open('numbers.txt', 'w') as f_obj:
    json.dump(names_numbers , f_obj);
