hellostring="""
1 загрузить из файла
2 сохранить в файл
3 добавить заметку
4 редактировать заметку
5 найти по записи
6 удалить заметку 
7 выйти из программы
введите номер команды:
"""
def save(db):
    pass
def need_save(flag_need_save,db,string):
    while flag_need_save:
        print(string)
        numbercomand=input()
        if is_number_int(numbercomand):
            if(int(numbercomand)==1 or int(numbercomand)==2):
                flag_need_save=False
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
if __name__ == '__main__':
    while 1 :
        print(hellostring)
        flag_correct_numercomand=False
        flag_exit=False
        flag_need_save=False
        db=[]
        while flag_correct_numercomand==False:
            numbercomand=input()
            if is_number_int(numbercomand):
                numbercomand=int(numbercomand)
                if  0<numbercomand and numbercomand < 8:
                    flag_correct_numercomand=True
                    if(numbercomand ==1):#команда загрузить
                        need_save(flag_need_save, db, "Вы хотите загрузить файл,но у вас есть не сохранные изменения.\nсохранить?\n1 да\n2 нет")
                    elif( numbercomand == 2):
                        save(db)
                        pass
                    elif(numbercomand==3):
                        pass
                    elif(numbercomand==4):
                        pass
                    elif(numbercomand==5):
                        pass
                    elif(numbercomand==6):
                        pass
                    else:#команда выхода
                        flag_exit=True
                else:
                    print("команды с таким номером нет")
            else:
                print("Был введен не номер команды")
            if flag_correct_numercomand==False:
                print("введите номер командыы заново")
        if flag_exit==True:
            break
