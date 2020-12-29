import json  # подключили библиотеку для работы с json
from types import SimpleNamespace as Namespace
from collections import namedtuple
from pprint import pprint  # подключили Pprint для красоты выдачи текста

with open('C:\\python\\users1.json', 'r', encoding='utf-8') as f:  # открыли файл с данными
    x = json.load(f, object_hook=lambda d: Namespace(**d))
    print(x.users[0].profile.email)
#    text = json.load(f)  # загнали все, что получилось в переменную




#print (x.name, x.hometown.name, x.hometown.id)

#for i in text['users']:
#    print(i['profile'])
    #print(i['profile'])
    #    print(i['id'], ' - ', i['name'])
