'''films=['Титаник','Люди в черном','История игрушек']
Score=[5,4,5,4,4,5]
cords=[[3,4,5],
       [4,5,7],
       [-3,5,-8]]

fav_films=[]
film_1=input()
film_2=input()
film_3=input()
fav_films.append(film_1)
fav_films.append(film_2)
fav_films.append(film_3)
lenght=len(fav_films)
print(len(fav_films))
print(fav_films)


factus=['Хамелеоны могут двигать глазами в разных направлениях одновременно','Змеи видят через веки','У коал отпечатки пальцев похожи на человеческие','Белые медведи - левши','Факт о себе']
choose=int(input('Выберете рандомный факт от 1 до 5: '))
if choose == 1 or choose == 5:
    print(factus[choose-1])
else:
    print(factus[choose])



numbers=[1,2,3,4]
minn=min(numbers)
'''

# random
'''import random
priv=['Привет!','Здравствуй!','Васап!']
num=random.randint(0,2)
print(priv[num])'''
'''
scores=[5,4,5,4,5,4,5]
avg=sum(scores)/len(scores)
mxm=max(scores)
mnm=min(scores)
cnt_5=scores.count(5)
print('Средняя оценка: ', avg)
print('Наивысшая оценка: ', mxm)
print('Наименьшая: ', mnm)
print('Количество пятёрок: ', cnt_5)'''

"""
lst = [-9, 150, 5435, -52546, 43849328, 0, -4, -9]
minn = 0   # для нахождения минимального элемента списка
cnt = 0    # для среза
for i in range(1, len(lst)):
    minn = min(lst[cnt::1]) # нахождение минимума на срезе
    lst[lst.index(minn)], lst[cnt] = lst[cnt], lst[lst.index(minn)]   # смена элементов местами
    cnt += 1
print(lst)"""
"""
just_nums = [-9, 150, 5435, -52546, 43849328, 0, -4, -9]
maxx = 0   # для нахождения минимального элемента списка
cnt = len(just_nums)+1  # для среза
for i in range(len(just_nums)+1):
    maxx = max(just_nums[0:cnt:1])   # нахождение минимума на срезе
    just_nums.append(maxx)
    just_nums.remove(maxx)
    cnt -= 1
just_nums.reverse()
print(just_nums)

"""
"""

Что нужно сделать:

Допишите калькулятор, добавьте функции умножения и деления. Все ответы должны сохраняться в текстовый документ. 
Оберните код калькулятора в функцию. Которая принимает три аргумента: два числа и операция. 

"""
"""
def calc():
    num_1_2_operr = input('число 1, операция, число 2: ').split()
    if num_1_2_operr[1] == '+':
        print(num_1_2_operr[0],'+',num_1_2_operr[-1],'=',int(num_1_2_operr[0]) + int(num_1_2_operr[-1]))
    elif num_1_2_operr[1] == '-':
        print(num_1_2_operr[0],'-',num_1_2_operr[-1],'=',int(num_1_2_operr[0])-int(num_1_2_operr[-1]))
    elif num_1_2_operr[1] == '*':
        print(num_1_2_operr[0],'*',num_1_2_operr[-1],'=',int(num_1_2_operr[0]) * int(num_1_2_operr[-1]))
    elif num_1_2_operr[1] == '/':
        print(num_1_2_operr[0],':',num_1_2_operr[-1],'=',int(num_1_2_operr[0]) / int(num_1_2_operr[-1]))

fl = open('txt_calc', 'w')
fl.write(str(calc()))

fl.close()

eval
"""

"""
num_1 = int(input())
num_2 = int(input())
operator = input()
def calc(num_1, num_2, operator):
    match operator:
        case "+":
            return num_1+num_2
        case "-":
            return num_1-num_2
        case "/":
            try:
                return num_1/num_2
            except ZeroDivisionError:
                print("Oops!  That was no valid number.  Try again...")
        case "*":
            return num_1*num_2
answer = calc(num_1,num_2, operator)
fl = open('txt_calc', 'a')
fl.write(str(answer))
fl.write('\n')
fl.close

"""

"""
В кругу стоят n человек, пронумерованных числами от 1 до n. Начинается расчет,
при котором каждый k-й по счету человек выбывает из круга, 
после чего счет продолжается со следующего за ним человека. 
Напишите программу, определяющую номер человека, который останется в кругу последним.
"""
"""
amount, xxcept = int(input()), int(input())
Survivors = []
for nomer in range(amount):
    Survivors.append(nomer+1)
cnt_of_xxcept = 1
person_now = 0
while len(Survivors) != 1:
    if person_now == len(Survivors):
        person_now = 0
    if cnt_of_xxcept == xxcept:
        cnt_of_xxcept = 0
    if cnt_of_xxcept % xxcept == 0:
        try:
            Survivors.remove(Survivors[person_now])
            person_now -= 1
        except ValueError:
            continue
    cnt_of_xxcept += 1
    person_now += 1
print(Survivors[0])"""


"""
lens_lst = int(input())
cnt_of_num = 1
numeracc = lens_lst**2
new_mtrx = 0
mtrixx = [[0]*lens_lst for i in range(lens_lst)]
ls = 0
while cnt_of_num != numeracc+1:
    print(lens_lst)
    for cnt in range(ls, lens_lst+ls):
        mtrixx[new_mtrx][cnt] = cnt_of_num
        cnt_of_num += 1
        if cnt == lens_lst-1:
            lens_lst -= 1
            for j in range(lens_lst):
                    new_mtrx += 1
                    mtrixx[new_mtrx][lens_lst] = cnt_of_num
                    cnt_of_num += 1
        if new_mtrx == lens_lst:
            for k in range(lens_lst):
                cnt -= 1
                mtrixx[new_mtrx][cnt] = cnt_of_num
                cnt_of_num += 1
        if (new_mtrx == lens_lst) and (cnt == 0):
            lens_lst -= 1
            for n in range(lens_lst):
                new_mtrx -= 1
                mtrixx[new_mtrx][cnt] = cnt_of_num
                cnt_of_num += 1
    ls += 1
    print(mtrixx)
    for i in range(len(mtrixx)):
        print(*mtrixx[i], sep=' ')
"""







"""
just_nums = [1, 4, -3, 0, 10]
maxx = 0   # для нахождения максимального элемента списка
cnt = len(just_nums)+1  # для среза
for i in range(len(just_nums)+1):
    maxx = max(just_nums[0:cnt:1])   # нахождение максимума на срезе
    just_nums.append(maxx)
    just_nums.remove(maxx)
    cnt -= 1
just_nums.reverse()
print(just_nums)


weather = int(input('Какое количество градусов на улице? \n'))
if weather < -15 :
    print('Очень холодно')
elif -10<weather<0:
    print('Холодно')
elif 0<=weather<10:
    print('Прохладно')
elif 10<=weather<17:
    print('тепло')
elif 17<=weather<25:
    print('Жарко')
elif 25<=weather:
    print('Очень жарко')
"""


x = -11//10
y=-11%10
print(x,y)















