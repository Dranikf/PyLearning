men = {'name' : 'Nikita' , 'second name': 'Tokarchyk' , 'age' : 19 , 'city' : 'Ivanovo',
        'favorite places' : ['Ivanovo' , 'Minsk']}
men2 = {'name' : 'Serhey' , 'second name': 'Ryhlin' , 'age' : 19 , 'city' : 'Vitebsk', 
        'favorite places' : ['Moskow' , 'Monako', 'Hyjako']}
men3 = {'name' : 'Nadejda' , 'second name': 'Rojkovets' , 'age' : 18 , 'city' : 'Ivanovo',
        'favorite places' : ['Spain' , 'Portugal'] }

people = [men , men2 , men3]

for i in list(range(0, len(people))):
    print('Info' + str(i) +'++++++++++++++');
    for key, item  in people[i].items():
        if(key == 'age'):
            info = str(item);
        elif (key == 'favorite places'):
            print(key + ':');
            for place in item:
                print('\t\t' + place);
            continue;
        else:
            info = item;
        print('\t' + key + ' : ' + info);
        
