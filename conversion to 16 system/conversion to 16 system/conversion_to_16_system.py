#проверка наличия ключа
def CheckKey(dictionary, val): 
    for key, value in dictionary.items():
        if key == val:
            return value
    return -1

#формирование числа в 16 ричной системе
def NewNumber(total, dictionary):
    string =''
    for t in total:
        if (CheckKey(dictionary, t) == -1):
            string += str(t)
        else:
            for key, value in dictionary.items():
                if t == key:
                    string += value
    return string

#работа
def Process(number):
    if number < 65536:
        total = []
        dictionary = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
        if number > 15:
            while number >= 15:
                balance = int(number / 16)
                numb = int(number - (16 * balance))
                total.insert(0, numb)
                number = balance
            total.insert(0, balance)           
            print(NewNumber(total, dictionary))
        else:
            check = CheckKey(dictionary, number)
            if (check == -1):
                print(number)
            else:
                print(check)
    else:
        print("Введенное число больше чем 65536")
#--------------------------------------------------------------------------------------------------------

print("Выполнил %%UserName%%, группа ЕМ-411.16, Вариант 10, Лабораторная работа номер 6, задача 2")
try:
    number = int(input('Введите число в десятичной системе счисления: '))
    print('Число в шестнадцатеричной системе счисления: ', end ='') 
    Process(number)
except ValueError:
    print("Нужно ввести число")
except Exception as err:
    print(err)

