import json  # подключили библиотеку для работы с json
from types import SimpleNamespace as Namespace
from collections import namedtuple
from pprint import pprint  # подключили Pprint для красоты выдачи текста

with open('C:\\python\\users1.json', 'r', encoding='utf-8') as f:  # открыли файл с данными

    text = json.load(f)  # загнали все, что получилось в переменную
    for i in text['users']:
        if i['is_bot'] == True:
            continue
        d = i['profile']
        d['email'] = 'aaabbb'
#        print(d['email'])
    #print(i['profile'])
    #    print(i['id'], ' - ', i['name'])
with open('C:\\python\\data.json', 'w') as outfile:
    json.dump(text, outfile)
