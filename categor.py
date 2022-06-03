import nltk
from fuzzywuzzy import fuzz as f
from fuzzywuzzy import process as p

opts = {'Hello':
            ['доброе утро', 'добрый день', 'добрый вечер!', 'здравствуйте', 'привет', 'как дела' ,'как поживаете'
                ,'утро','добрый', 'приветствую'],
    'Goodbye':
        ['пока', 'до встречи', 'удачи', 'спокойной ночи','доброй ночи',' спокойного сна',
         ' аревуар',' чао','всего доброго', 'всего хорошего', 'счастливо', 'чао-какао'],
        "cmds": {
            "firs": ['текущее время', 'сейчас времени', 'который час'],
            "second": ['включи музыку', 'воспроизведи радио', 'включи радио'],
            "third": ['расскажи анекдот', 'рассмеши меня', 'ты знаешь анекдоты']
        }
        }
cmds ={
            "firs": ['текущее время', 'сейчас времени', 'который час'],
            "second": ['включи музыку', 'воспроизведи радио', 'включи радио'],
            "third": ['расскажи анекдот', 'рассмеши меня', 'ты знаешь анекдоты']
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
        return '0'


def categor(msg):
    percent= (p.extract(msg, opts, limit=3))
    prc = []
    for i in percent:
        prc_str = [int(i[1]),str(i[2])]
        prc.append(prc_str)
    if (prc[0][0] - prc[1][0]) > 10:
        if prc[0][1] == 'cmds':
            return categor_cmds(msg)

        return prc[0][1]

    else:
        return '0'


while True:
    print(categor(input(':')))

