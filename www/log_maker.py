# -*- coding: utf-8 -*
# log_maker

import os
import datetime
import ast

from telebot import types

"""
Пред подготовка
"""

# Создает папку logs
folder_path = os.environ['PWD'] + '/logs'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Обьявление путей к файлам (для их создания и не только)
log_path = os.environ['PWD'] + '/logs/log ' + str(datetime.datetime.now())[:-7] + '.txt'
new_book_path = os.environ['PWD'] + '/logs/new_book.txt'
stats_path = os.environ['PWD'] + '/logs/statistics.txt'

# Создание нового лога
f = open(log_path, 'w')
txt = '* * * * * * * * * * * * * *\n'
txt = txt + str(datetime.datetime.now()) + '\n'
txt = txt + '* * * * * * * * * * * * * *\n\n'
print(txt)
f.write(txt)
f.close()
del f, txt

"""
Создание и проверка new_book
"""
f = open(new_book_path, 'a')  # Создает файл при его отсутствии
f.close()
f = open(new_book_path, 'r')    # Проверка содержимого на неисправность
x = f.read()       # Содержимое
if x.count('\n') != 0:
    n = x.index('\n')   # Индекс первого пробела
else:
    n = None
try:
    if n is not None:
        y = ast.literal_eval(x[:n])
    else:
        y = ast.literal_eval(x)
except SyntaxError:
    y = None
except NameError:
    y = None
except ValueError:
    y = None

if y is None:  # Если неисправный файл
    f.close()
    f = open(new_book_path, 'w')
    x = '{}\n' + x
    f.write(x)
f.close()
del f, x, y

"""
Создание и проверка stats
"""
f = open(stats_path, 'a')  # Создает файл при его отсутствии
f.close()
f = open(stats_path, 'r')    # Проверка содержимого на неисправность
x = f.read()       # Содержимое
if x.count('\n') != 0:
    n = x.index('\n')   # Индекс первого пробела
else:
    n = None
try:
    if n is not None:
        y = ast.literal_eval(x[:n])
    else:
        y = ast.literal_eval(x)
except SyntaxError:
    y = None
except NameError:
    y = None
except ValueError:
    y = None

if y is None:  # Если неисправный файл
    f.close()
    x = '{}\n' + x
    f = open(stats_path, 'w')
    f.write(x)
f.close()
del f, x, y


"""
Функции
"""


# Основной лог
def log(mess=None, text=None, date=False):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    log_text = ''
    if date:
        log_text = log_text + str(datetime.datetime.now())
    if mess is not None:
        # print(mess)
        log_text = datetime.datetime.fromtimestamp(mess.date).strftime('%Y-%m-%d %H:%M:%S') + '\n'
        if text is not None:
            log_text = log_text + '\tКомментарии:\n\t' + str(text) + '\n'
        if mess.content_type == 'text':
            log_text = log_text + '\tmID: {0}, uID: {1}, User: {3}, l:{5}\n' \
                                  '\tСообщение от {2} {4}:\n' \
                                  '\t{6}\n' \
                                  '\n'.format(mess.message_id,
                                              mess.from_user.id,
                                              mess.from_user.first_name,
                                              mess.from_user.username,
                                              mess.from_user.last_name,
                                              mess.from_user.language_code,
                                              mess.text)
        elif mess.content_type == 'audio':
            log_text = log_text + '\tmID: {0}, uID: {1}, User: {3}, l:{5}\n' \
                                  '\tАудиофайл от {2} {4}:\n' \
                                  '\tID: {6}\n' \
                                  '\t{8} ({7})\n' \
                                  '\t{9}\n' \
                                  '\n'.format(mess.message_id,               # 0
                                              mess.from_user.id,             # 1
                                              mess.from_user.first_name,
                                              mess.from_user.username,
                                              mess.from_user.last_name,      # 4
                                              mess.from_user.language_code,
                                              mess.audio.file_id,
                                              str(datetime.timedelta(seconds=mess.audio.duration)),   # 7
                                              mess.audio.performer,
                                              mess.audio.title,
                                              mess.audio.mime_type,          # 10
                                              mess.audio.file_size)
    print(log_text)
    f0 = open(log_path, 'a')
    f0.write(log_text)
    f0.close()


# Создание dict при загрузке новой книги
def new_book_log(a, b):
    f1 = open(new_book_path, 'r')
    t = f1.read()
    f1.close()
    t = ast.literal_eval(t)
    z = str(len(t)) + '. ' + str(a)
    t[z] = b
    f1 = open(new_book_path, 'w')
    f1.write(str(t))
    f1.close()


# Запись статистики
def stats(mess):
    f2 = open(stats_path, 'r')
    x0 = f2.read()
    f2.close()
    if x0.count('\n') != 0:
        n0 = x0.index('\n')
    else:
        n0 = None
    if n0 is None:
        sts = ast.literal_eval(x0)
    else:
        sts = ast.literal_eval(x0[:n0])
    name = str(mess.from_user.id) + ':' + mess.from_user.username
    if sts.get(name) is None:
        sts[name] = 1
    else:
        sts[name] = sts[name] + 1
    x0 = str(sts) + x0[n0:]
    f2 = open(stats_path, 'w')
    f2.write(x0)
    f2.close()
