guests_names = ['Saitama' , 'Poya' , 'Linus']
message = 'invite for launch with me '

def showGuestsMessage(mes):
    for guest in guests_names:
        print(mes + guest)

showGuestsMessage(message);

print('\n')
print(guests_names.pop(1) + ' cant be at lunch \n');
guests_names.append('terror reid');


print('new guests list');
showGuestsMessage(message)


print('\n we have more guests')
guests_names.insert(0 , 'skoobi-doo')
guests_names.insert(2 , 'spange bob')
guests_names.append('my girl friend')


showGuestsMessage(message)

print('its not enought places for gusts')
message = 'sorri you is deleted'

guests_names2 = [];
guests_names2.append(guests_names.pop(0));
guests_names2.append(guests_names.pop(0));

print('\n')
showGuestsMessage(message)

guests_names = guests_names2;
showGuestsMessage('its ok for you ')


del guests_names[0];
del guests_names[0];


print('\nend of the programm ')
print(guests_names)
