import nltk
from fuzzywuzzy import fuzz as f
from fuzzywuzzy import process as p

opts = {'Hello':
            ['доброе утро', 'добрый день', 'добрый вечер!', 'здравствуйте', 'привет', 'как дела' ,'как'
                ,'утро','добрый', 'приветствую'],
    'Goodbye':
        ['пока', 'до встречи', 'удачи', 'спокойной ночи','доброй ночи',' спокойного сна',
         ' аревуар',' чао','всего доброго', 'всего хорошего', 'счастливо', 'чао-какао'],
        "cmds": {
            "firs": ['айфон', 'телефон', 'андройд','мобила','трубка','звонилка','номер','iphone','apple'],
            "second": ['ПК', 'пк', 'Ноут','персональный компьютер','Компьютер','macbook','mac'],
            "third": ['планшет', 'айпад', 'ipad','айпадик','планшетик']
        }
        }
cmds ={
            "firs": ['айфон', 'телефон', 'андройд','мобила','трубка','звонилка','номер','iphone','apple'],
            "second": ['ПК', 'пк', 'Ноут','персональный компьютер','Компьютер','macbook','mac'],
            "third": ['планшет', 'айпад', 'ipad','айпадик','планшетик']
}

def categor_cmds(msg):
    percent = (p.extract(msg, cmds, limit=3))
    prc = []
    for i in percent:
        prc_str = [int(i[1]),str(i[2])]
        prc.append(prc_str)
    if (prc[0][0] - prc[1][0]) > 10:
        return prc[0][1]
    else:
        return '01'


def categor(msg):
    percent= (p.extract(msg, opts, limit=3))
    prc = []
    for i in percent:
        prc_str = [int(i[1]),str(i[2])]
        prc.append(prc_str)
    if (prc[0][0] - prc[1][0]) > 15:
        if prc[0][1] == 'cmds':
            return categor_cmds(msg)

        return '0'

    else:
        return prc



