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
					flag_correct_numercomand=True
					pass
				else:
					print("Был введен не номер команды\n")
				if flag_correct_numercomand==False:
					print("введите номер командыы заново")