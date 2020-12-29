import json
import re

# Opening JSON file
f = open('C:\\python\\users1.json')
f1 = open('C:\\python\\1.txt')
data = json.load(f)

for txt in f1:
    print(txt)
    txt = txt.rstrip('\n')
    result = re.split(r'\t', txt, maxsplit=1)
    for i in data['users']:
        if i[]

#for i in data['users']:
#    print(i['id'], ' - ', i['name'])


# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
#for i in data['users']:
#    print(i['id'], ' - ', i['name'])

# Closing file
#f.close()