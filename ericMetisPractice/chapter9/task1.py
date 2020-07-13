
class Restautant():
    
    def __init__(self ,restaurant_name , cuisine_type):
        self.name = restaurant_name;
        self.type = cuisine_type;

    def describe_estaurant(self):
        print('Restaurant name is: ' + self.name);
        print('Restaurant type is: ' + self.type)

    def open_restaurant(self):
        print('Restautant ' + self.name + ' is open');



hello = Restautant('name', 'type');

print(hello.name);
print(hello.type);

hello.describe_estaurant();
hello.open_restaurant();

restaurant2 = Restautant('grand cafe', 'elite');
restaurant3 = Restautant('el pizza' , 'fast food');
print('\nrestaurant1 info');
restaurant2.describe_estaurant();
print('\nrestaurant2 info');
restaurant3.describe_estaurant();


class IceCreamStand(Restautant):

    def __init__(self, restaurant_name):
        super().__init__(restaurant_name , 'stand');
        self.flavours = ['vanilla' , 'chokolate' , 'rasberry'];

    def printFlavours(self):
        for flavour in self.flavours:
            print(flavour);


print('\n ice cream stand info')
stand1 = IceCreamStand('finny ymmy')
stand1.describe_estaurant();
stand1.printFlavours();
