"""
eng_dict ={
    'Яблоко':'apple',
    'Молоко':'milk',
    'Кот':'cat',
}
print(eng_dict['яблоко'])
word=input('Введите слово на русском языке: \n')
if word in eng_dict:
    print(word+' на английском языке будет '+eng_dict[word])
else:
    print('Такого слова не существует хихихаха:)')

.lower() - регистр вниз
.upper() - регистр вверх
"""
"""
films_dict = {
    'Начало': 'Леонардо Ди Каприо',
    'Пираты Карибского моря': 'Джонни Депп',
    'Миссия невыполнима': 'Том Круз',
}
fav_actor = 'Леонардо Ди Каприо'
film = input('Какой фильм собираетесь посмотреть? \n')
actor = films_dict.get(film)  # get вытаскивает значение по ключу
if film not in films_dict:
    print('иди нахуй')
elif actor == fav_actor:
    print('Этот фильм точно стоит посмотреть!')
else:
    print('Говно, залупа, пенис, хер, давалка, хуй, блядина')
"""
"""
Или
if film in films_dict:
    actor == films_dict.get(film)
    if actor == fav_actor:
        print('Этот фильм точно стоит посмотреть!')
    else:
        print('Говно, залупа, пенис, хер, давалка, хуй, блядина')
else:
    print('Такого фильма нет в нашей базе')


questions = [
    {'quest': 'Игра с лучшим, добрым коммьюнити',
     'answers': ['Rust', 'Dota2', 'LoL', 'Сверхъестественное'],
     'right_answer':2},
     {'quest':'Игра, где очень важна командная составляющая',
      'answers':['Tom Clancy's','Hollow Knight','Dota2','Pycharm' ],
      'right_answer':3},
      {'quest':'Игра где люди маленького рейтинга любят пропускат ьпромежуточные предметы',
       'answers':['Witcher 3','Dota2','Магическая битва','Садистская смесь'],
       'right_answer':2} 
]
for quest in questions:
    print(questions.get('quest'))
    answer_number = 0
    for answer in quest['answers']:
        answer_number += 1
        print(answer_number, '. ', answer)
    user_answer = int(input('Ваш ответ: '))
    if user_answer == quest.get('right_answer'):
        print('Верно')
    else:
        print('Неверно')
    
"""

questions = [
    {'quest': 'Игра с лучшим, добрым коммьюнити',
     'answers': ['Rust', 'Dota2', 'LoL', 'Сверхъестественное'],
     'right_answer':2},
     {'quest':'Игра, где очень важна командная составляющая',
      'answers':['Tom Clancy','Hollow Knight','Dota2','Pycharm' ],
      'right_answer':3},
      {'quest':'Игра где люди маленького рейтинга любят пропускать промежуточные предметы',
       'answers':['Witcher 3','Dota2','Магическая битва','Садистская смесь'],
       'right_answer':2}
]

for quest in questions:
    print(quest.get('quest'))
    answer_number = 0
    for answer in quest['answers']:
        answer_number += 1
        print(answer_number, '. ', answer)
    user_answer = int(input('Ваш ответ: '))
    if user_answer == quest.get('right_answer'):
        print('Верно')
    else:
        print('Неверно')
    print('-'*20)



