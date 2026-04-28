from Backend.database.install_DB 
import sqlite3



def install_log_system(level,name,text):
    if level == "error": error_log(name,text)
    elif level == "war": warrning_log(name,text)
    elif level == "good": good_log(name,text)
    else: error_log("Error log system","Ошибка")


def error_log(name,text):
    ...
    #with sqlite3.connect(database_name) as conn:
       # ...
        #и всё мы тут короче записываем и готово
   # print(f'\033[31m{name} - {text}\033[0m')


def warrning_log(name,text):
    ...
    #with sqlite3.connect(database_name) as conn:
        #...
       # #и всё мы тут короче записываем и готово
    #print(f'\033[33m{name} - {text}\033[0m')


def good_log(name,text):
    with sqlite3.connect(database_name) as conn:
        ...
        #и всё мы тут короче записываем и готово
    print(f'\033[32m{name} - {text}\033[0m')
