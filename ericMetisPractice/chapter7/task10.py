user_place = {};

while True:
    name = input('enter your name ');
    place = input('enter place where you vant to rest');
    user_place[name] = place;
    
    if input('is it will be more information (yes/no)' ) == 'no':
        break;

print('\n RESULTS++++++++++++++++++')
for key, item in user_place.items():
    print(key + ' want go to ' + item);

