from random import randint;

class Die():
    def __init__(self , num):
        if(num < 1):
            self.num = 1;
            return;
        self.num = num;

    def roll_die(self):
        return randint(1 , self.num);


d = Die(6);
for i in list(range(1 ,11)):
    print(d.roll_die());

print('10 sides cube');
d = Die(10);
for i in list(range(1, 11)):
    print(d.roll_die());

print('20 sides cube');
d = Die(20);
for i in list(range(1, 11)):
    print(d.roll_die());
