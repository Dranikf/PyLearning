import json;

with open('jsonFile.json') as f_obj:
    numbers = json.load(f_obj);

class hello():
    def __init__(self, dest , a):
        self.dest = dest;
        self.a = a;


