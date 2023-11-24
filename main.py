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
			while flag_correct_numercomand==False:
				numbercomand=input()
				if is_number_int(numbercomand):
					numbercomand=int(numbercomand)
					if  0<numbercomand and numbercomand < 8:
						flag_correct_numercomand=True
						if(numbercomand ==1):
							pass
						elif( numbercomand == 2):
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
					print("Был введен не номер команды\n")
				if flag_correct_numercomand==False:
					print("введите номер командыы заново")
			if flag_exit==True:
				break
