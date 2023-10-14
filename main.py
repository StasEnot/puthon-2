import random
user = {'Stas':'1010'}
print('Створити новий акаунт чи Увійти (Новий/Увійти)')
sign=input()
if sign == "Новий":
 print('Напишіть ваш логін ')
 user_a_login = input()
 print('Напишіть ваш  пароль ')
 user_a_password = input()
 user[user_a_login]=user_a_password
 print('ви створили новий акаунт тепер можуту війти у нього')
 print('Ведіть логін')
 log = input()
 print('Ведіть пароль')
 password = input()
 print('ви війшли')

 if user[log] == password:
  answ = ('Так', 'ні', 'Можливо', 'точно спробуй', 'сім раз відмірй і один відріж')
  point = 0
  print('Отримати відповідь? (Так/Ні)')
  word = input()
  while word == 'Так':
   print(answ[random.randint(0, 4)])
   print()
   print("Отримати відповідь? (Так/Ні)")
   word = input()
   point += 1
   if point == 3:
    print("На сьогодні ти використав всі відповідь спробуй завтра")
    break
elif sign == "Увійти":


 print('Ведіть логін')
 log = input()
 print('Ведіть пароль')
 password = input()

 if user[log] == password:
    answ = ('Так', 'ні', 'Можливо', 'точно спробуй', 'сім раз відмірй і один відріж')
    point = 0
    print('Отримати відповідь? (Так/Ні)')
    word = input()
    while word == 'Так':
        print(answ[random.randint(0, 4)])
        print()
        print("Отримати відповідь? (Так/Ні)")
        word = input()
        point += 1
        if point == 3:
            print("На сьогодні ти використав всі відповідь спробуй завтра")
            break

else:
    print('ви вели неправиоьний пароль')
