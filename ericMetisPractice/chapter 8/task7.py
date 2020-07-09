def make_albom(singer , name , tracksCount = 0):
    result = {'singer' : singer ,
                'name' : name}
    if(tracksCount != 0):
        result['tracksCount'] = tracksCount
    return result;


al1 = make_albom('ramshtein' , 'du hust');
al2 = make_albom('ssshhhiiittt' , 'asidsun' , 6);
    
print(al1);
print(al2);

alboms = [];

while True:
    name  = input('Enter albom name: ');
    singer = input('Enter singer: ');
    
    alboms.append({'name' : name , 'singer' : singer});

    q = input('Exit program (yes)');
    if(q == 'yes'):
        break;


print('Entered singers \n');
for albom in alboms:
    print(albom);
