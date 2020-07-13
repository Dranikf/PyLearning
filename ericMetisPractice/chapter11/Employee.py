class Employee():

    def __init__(self, name, second_name, year_payment):
        self.name = name;
        self.second_name = second_name;
        self.year_payment = year_payment;

    def give_raise(self, value = 5000):
        self.year_payment += value;
