    
try:
    with open('cats.txt') as cats:
        print(cats.read());

    with open('dogs.txt') as dogs:
        print(dogs.read());
except FileNotFoundError:
    print('cant fid one of nessesary files');
