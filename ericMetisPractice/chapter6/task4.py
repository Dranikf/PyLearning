rivers = {'Nile' : 'Egypt' , 'Amazonka': 'Brazil' , 'Dnepr' : 'Ukrain'}

for river, place in rivers.items():
    print('\nriver name: ' + river);
    print('country: ' + place);


print('\nRiver names');
for river in rivers.keys():
    print(river);

print('\nRiver places');
for place in rivers.values():
    print(place);
    
