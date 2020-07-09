magicians = ['Fedor' , 'Kobak' , 'Alekseevich'];

def magShow(magicians):
    for magician in magicians:
        print(magician);

def makeGreat(magicians , greatMagic):
    for magician in magicians:
        greatMagic.append('Great' + magician);

magShow(magicians);

print('\nMaking great');
greatMagic = [];
makeGreat(magicians, greatMagic);
magShow(greatMagic);
