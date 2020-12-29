import json  # подключили библиотеку для работы с json
import re
from types import SimpleNamespace as Namespace
from collections import namedtuple
from pprint import pprint  # подключили Pprint для красоты выдачи текста

f1 = open('C:\\python\\1.txt')

with open('C:\\python\\users1.json', 'r', encoding='utf-8') as f:
    text = json.load(f)  # загнали все, что получилось в переменную
    for txt in f1:
#        print(txt)
        txt = txt.rstrip('\n')
        result = re.split(r'\t', txt, maxsplit=1)

        for i in text['users']:
            if i['is_bot'] == True:
                continue
            d = i['profile']
            if d['email'] == result[0]:

                print(d['email'], '-' , result[1])
                d['email'] = result[1]
                continue
with open('C:\\python\\data.json', 'w') as outfile:
    json.dump(text, outfile)