from random import randint

""" 
привет, любопытный варовец, решивший запустить этот файл в рандомном редакторе, дабы узнать, что же тут за вакханалия происходит...
я, порядком, не ожидала, что ты решишься пойти на ТАКОЕ, ну, в плане, зачем... это так гениально с твоей стороны, как гениально с моей стороны оставить эту записку
как ты видишь, в программировании я новичок, код большой, однако им я горжусь! все с чего-то начинают, и сделать подобное - непросто, да?
можешь добавлять сюда что-то своё, поделиться этим в комментариях к посту, заодно поделись впечатлениями, и вообще, удивлен ли ты тому, что я предугадала твои действия?
может, ты тоже оставишь записку, если решишь что-то добавить... возможно я о ней узнаю.. сообщество программистов , давайте оставлять тут записки и общаться таким образом, открывая файлы в редакторах....

"""

def pole():
    print(' ', "__" * len(x_copy[0]))
    for a in range(len(x_copy)):
        print('|', end=' ')
        print(*x_copy[a], "|")
    print(' ', "__" * len(x_copy[0]))   
    
def opaski(): #стремное, и что.
    if num[0] != 0:
        saper.append(x[num[1]][num[0] - 1])
    if num[0] != len(x_copy[0]) - 1:
        saper.append(x[num[1]][num[0] + 1])
    if num[1] != 0:
        saper.append(x[num[1] - 1][num[0]])
    if num[1] != len(x_copy) - 1:
        saper.append(x[num[1] + 1][num[0]])
    if num[0] != len(x_copy[0]) - 1 and num[1] != len(x_copy) - 1:
        saper.append(x[num[1] + 1][num[0] + 1])
    if num[0] != len(x_copy[0]) - 1 and num[1] != 0:
        saper.append(x[num[1] - 1][num[0] + 1])    
    if num[0] != 0 and num[1] != 0:
        saper.append(x[num[1] - 1][num[0] - 1])
    if num[0] != 0 and num[1] != len(x_copy) - 1:
        saper.append(x[num[1] + 1][num[0] - 1])
        
def pobeda():
    haha = 0
    for index in range(len(x_copy)):
        haha += x_copy[index].count("О")
    

number = randint(10, 20)
            

x = [["О" for a in range(number)] for a in range(number)]
x_copy = [["О" for a in range(number)] for a in range(number)]
saper = list()
haha = 1

for a in range(randint(5, len(x) * len(x[0]) - 10)):
    randx = randint(0, len(x[0]) - 1)
    randy = randint(0, len(x) - 1)
    while x[randy][randx] == "Х":
        randx = randint(0, len(x[0]) - 1)
        randy = randint(0, len(x) - 1)
    x[randy][randx] = "Х"
    
pole()
print("Привет! Если хочешь отметить опасную клетку, после координат укажи '1'. Отметки убирать МОЖНО, если сделать по ним атаку!")
print(f"Если хочешь сделать ход - после указания координат отметь '2'. Поле сапёра - {len(x_copy)} клеток в квадрате. Удачи с игрой!")
while haha > 0:
    num = input("Введи координаты поля с пробелами: ").split()
    if len(num) < 3:
        print("Мало данных ввёл")
    else:
        if not num[0].isdigit() or not num[1].isdigit():
            print("Ты некорректное что-то ввёл")
        else:
            num[0] = int(num[0]) - 1
            num[1] = int(num[1]) - 1
            if num[0] >= len(x_copy[0]) or num[1] >= len(x_copy) or num[0] + 1 == 0 or num[1] + 1 == 0:
                print('Оооу, координаты не подходят...')
            else:
                if num[2] != "2" and num[2] != "1":
                    print("Система защищена от дураков. ты вызвал несуществующую функцию!")
                else:
                    if num[2] == "1":
                        x_copy[num[1]][num[0]] = "Х"
                        pobeda()
                        pole()
                        print("Надеемся, ты правильную клетку отметил.")
                    else:
                        if x[num[1]][num[0]] == "Х":
                            x_copy[num[1]][num[0]] = "Х"
                            haha = -1
                            pole()
                        else:
                            opaski()
                            x_copy[num[1]][num[0]] = saper.count("Х")
                            saper = []
                            pobeda()
                            pole()
                            print("Повезло! Но не время останавливаться... ")
if haha == -1:
    print("Ты умер, герой. но тем не менее.....")
elif haha == 0:
    print("Ты победил, молодец! и, кстати...")
print("Спасибо за игрууу!")