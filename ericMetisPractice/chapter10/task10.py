
def countWordInFile(fileName, word):
    with open(fileName) as text:
        num = text.read().lower().count(word);
    
    print(fileName + ' has '+ str(num) + ' "' + word + '"');


countWordInFile('alice.txt', 'the')
