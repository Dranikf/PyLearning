
with open('learning_python.txt') as helloFile:
    lines = helloFile.readlines();

def printLines(lines):
    for line in lines:
        print(line.rstrip());

def printReplaceLines(lines , old , new):
    for line in lines:
        print(line.rstrip().replace(old , new));


printLines(lines);
print('\n');
printLines(lines);
print('\n');
printLines(lines);

print('\n TASK2 \n');

printReplaceLines(lines, 'python' , 'fuck');
print('\n');
printReplaceLines(lines, 'python' , 'fuck');
print('\n');
printReplaceLines(lines, 'python' , 'fuck');
