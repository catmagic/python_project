import json

from  note import *
from datetime import date, datetime
import time
hellostring="""
1 загрузить из файла
2 сохранить в файл
3 добавить заметку
4 редактировать заметку
5 найти заметки по дате
6 читать по номеру заметки
7 удалить заметку 
8 вывести заголовки и id всех сообщений
9 выйти из программы
введите номер команды:
"""

def add_note(db):
    maxid = max(db, key=lambda mynote : mynote.id, default=MyNote(0,1,1,1,1)).id
    id = maxid+1
    title = input("Введите заголовок\n")
    mynote = input("Введите тело заметки\n")
    sec = time.time()
    struct = time.localtime(sec)
    stime = time.strftime('%H:%M:%S', struct)
    db.append(MyNote(id, title, mynote, date.today().strftime("%d/%m/%Y"), stime))

def save(db):
    namefile = input("введите имя файла\n")
    f = open(namefile, "w")
    f.write(json.dumps(db, cls=MyNoteEncoder))
    f.close()
def load(db,flag_need_save):
    namefile = input("введите имя файла\n")
    s = ""
    try:
        f = open(namefile, "r")
        for line in f:
            s += line
        f.close()
        db = json.loads(s)
        flag_need_save = False
    except IOError:
        print("нет файла. выход из загрузки файла.")

def need_save(flag_need_save,db,string):
    while flag_need_save:
        print(string)
        numbercomand = input()
        if is_number_int(numbercomand):
            if int(numbercomand) == 1 or int(numbercomand) == 2:
                flag_need_save = False
                if int(numbercomand) == 1:
                    save(db)
            else:
                print("команды с таким номером нет")
        else:
            print("Был введен не номер команды")
            
        
        
def is_number_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def edits(flag_need_save,db):
    while len(db):
        s = input("введите айди")
        if is_number_int(s):
            flag_exit_mynote = False
            index = 0
            for i in range(len(db)):
                if(db[i].id == int(s)):
                    flag_exit_mynote = True
                    index = i
                    break
            if(flag_exit_mynote):
                db[index].title = input("Введите заголовок\n")
                db[index].mynote = input("Введите тело заметки\n")
                sec = time.time()
                struct = time.localtime(sec)
                db[index].time = time.strftime('%H:%M:%S', struct)
                db[index].date = date.today().strftime("%d/%m/%Y")
                break
            else:
                print("с таким айди записи нет")
        else:
            print("айди это число")
    if(len(db)):
        flag_need_save = True
    else:
        print("база заметок пуста пуста")


def finddate(db):
    while len(db):
        s = input("введите дату в формате %d/%m/%Y\n")
        try:
            datetime.strptime(s, "%d/%m/%Y")

            flag_exit_mynote = False
            indexlist = []
            for i in range(len(db)):
                if (db[i].date == s):
                    flag_exit_mynote = True
                    indexlist.append(i)

            if (flag_exit_mynote):
               for index in indexlist:
                    print(str(db[index].id) + ":" + db[index].title)
            else:
               print("с такой датой записи нет")
            break

        except:
            print("не правильный формат даты")
    if (len(db) == 0):
        print("база заметок пуста пуста")
def findid(db):
    while len(db):
        s = input("введите айди\n")
        if is_number_int(s):
            flag_exit_mynote = False
            index = 0
            for i in range(len(db)):
                if (db[i].id == int(s)):
                    flag_exit_mynote = True
                    index = i
                    break
            if (flag_exit_mynote):
                print(str(db[index].id) + ":" + db[index].title+"\n"+db[index].note)

            else:
                print("с таким айди записи нет")
            break

        else:
            print("айди это число")
    if (len(db) == 0):
        print("база заметок пуста ")

def remove(flag_need_save, db):
    while len(db):
        s = input("введите айди\n")
        if is_number_int(s):
            flag_exit_mynote = False
            index = 0
            for i in range(len(db)):
                if (db[i].id == int(s)):
                    flag_exit_mynote = True
                    index = i
                    break
            if (flag_exit_mynote):
                db.pop(index)
                break
            else:
                print("с таким айди записи нет")

        else:
            print("айди это число")
    if (len(db) == 0):
        print("база заметок пуста ")

if __name__ == '__main__':
    db = []
    while 1 :
        print(hellostring)
        flag_correct_numercomand = False
        flag_exit = False
        flag_need_save = False
        while flag_correct_numercomand == False:
            numbercomand = input()
            if is_number_int(numbercomand):
                numbercomand = int(numbercomand)
                if  0 < numbercomand and numbercomand < 10:
                    flag_correct_numercomand=True
                    if numbercomand == 1: #команда загрузить
                        need_save(flag_need_save, db, "Вы хотите загрузить файл,но у вас есть не сохранные изменения.\nсохранить?\n1 да\n2 нет")
                        load(db,flag_need_save)
                    elif numbercomand == 2:
                        save(db)
                        flag_need_save = False
                    elif numbercomand == 3:
                        add_note(db)
                        file_need_save = True
                        pass
                    elif numbercomand == 4:
                        edits(file_need_save, db)
                    elif numbercomand == 5:
                        finddate(db)
                    elif numbercomand == 6:
                        findid(db)
                    elif numbercomand == 7:
                        remove(flag_need_save,db)
                    elif numbercomand == 8:
                        if(len(db)):
                            for  mynote in db:
                                print(str(mynote.id)+":"+mynote.title)
                        else:
                            print("заметок нет")
                    else:#команда выхода
                        flag_exit = True
                else:
                    print("команды с таким номером нет")
            else:
                print("Был введен не номер команды")
            if flag_correct_numercomand==False:
                print("введите номер командыы заново")
        if flag_exit == True:
            need_save(flag_need_save,db,"Вы хотите выйти, но у вас есть не сохранные изменения.\nсохранить?\n1 да\n2 нет")
            break
