glossary = {'template ' : 'its function or class that can work with different types',
            'function' : 'extract of code that can be used in defferent parts of programm',
            'list': 'dynamic array in Python',
            'string' : 'sequence of symbols',
            'hello world' : 'initial programm that shows that system works fine'};

keys = glossary.keys();

print('++++++++++GLOSSARY NAMES+++++++++++++')
for key in keys:
    print('--------' + key + '----------');
    print(glossary[key])
