class Privilages():
    def __init__(self , privilages):
        self.privilages = privilages; 


    def printPrivileges(self):
        for privilege in self.privilages:
            print('\t' + privilege);
 

class User():
    def __init__(self , login ,first_name , second_name, last_visit, privilages = []):
        self.first_name = first_name;
        self.second_name = second_name;
        self.last_visit = last_visit;
        self.login = login;
        self.login_attemps = 0;
        self.priviliges = Privilages(privilages);

    def describe_user(self):
        print('info of user "' + self.login + '":');
        print('\tUser first name: ' + self.first_name);
        print('\tUser second name: ' + self.second_name);
        print('\tlast visit: ' + self.last_visit);

    def greet_user(self):
        print('Hello ' + self.first_name + ' your last visit is: ' + self.last_visit);

    def increment_number_attemps(self):
        self.login_attemps += 1;

    def reset_login_attemps(self):
        self.login_attemps = 0;

    def setPriviliges(self , priviliges):
        self.priviliges = priviliges;

           

petor = User('boobs lover 69' , 'petor' , 'rusetski' , '2015-05-23');
petor.describe_user();
print('');
petor.greet_user();
print('');
fedor = User('FED' , 'fedor' , 'kobak' , '2016-03-12', ['kill users' , 'harm users' , 'ban users']);
fedor.describe_user();
print('');
fedor.greet_user();


fedor.increment_number_attemps();
fedor.increment_number_attemps();
fedor.increment_number_attemps();
fedor.increment_number_attemps();
print(fedor.login_attemps);

fedor.reset_login_attemps();
print(fedor.login_attemps);

print('privilages:');
fedor.priviliges.printPrivileges();
