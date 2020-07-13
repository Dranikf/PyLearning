import json

numbers = list(range(1,21, 3));

with open('jsonFile.json', 'w') as f_obj:
    json.dump(numbers, f_obj);
