
guestsNames = [];

while True:
    info = input('Enter Name, or nothing to stop the program');
    if info == '':
        break;
    guestsNames.append(info+'\n');


with open('guests.txt', 'a') as gFile:
   gFile.writelines(guestsNames);
