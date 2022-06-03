import nltk
from fuzzywuzzy import fuzz as f
from fuzzywuzzy import process as p


Hello =  ['доброе утро', 'добрый день', 'добрый вечер!', 'здравствуйте', 'привет', 'как дела' ,'как поживаете'
                ,'утро','добрый', 'приветствую']
Goodbye = ['пока', 'до встречи', 'удачи', 'спокойной ночи','доброй ночи',' спокойного сна',
         ' аревуар',' чао','всего доброго', 'всего хорошего', 'счастливо', 'чао-какао']


'''
            "firs": ['текущее время', 'сейчас времени', 'который час'],
            "second": ['включи музыку', 'воспроизведи радио', 'включи радио'],
            "third": ['расскажи анекдот', 'рассмеши меня', 'ты знаешь анекдоты']
        }
        }'''



# nltk.word_tokenize
# sentence = """At eight o'clock on Thursday morning
# ... Arthur didn't feel very good."""
sentence = 'hi'

tokens = nltk.word_tokenize(sentence)
print(tokens)


(p.extract("привет друг", Hello, limit=3))


def recognize_cmd(opts,sentence):
    RC = {'cmd': '', 'percent': 0}
    for c, v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(sentence, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt

