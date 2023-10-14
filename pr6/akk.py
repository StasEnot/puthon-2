import random
user = {'Stas':'1010'}
print('Створити новий акаунт чи Увійти (1-Новий 2-Увійти 3-Видалити)')
sign=input()
if sign == "1":
 print('Напишіть ваш логін ')
 user_a_login = input()
 print('Напишіть ваш  пароль ')
 user_a_password = input()
 user[user_a_login]=user_a_password
 print('ви створили новий акаунт тепер можуту війти у нього')
 print()
 print('Ведіть логін')
 log = input()
 print('Ведіть пароль')
 password = input()
 print('ви війшли')
 print("Ви може вийти або видалити акаунт або Ортимати Відповідь")
 delet1 = input()
 if delet1 == "Видалити" or delet1 == "видалити":
    print("Ви точно хочете видалити акаунт? (Так/Ні)")
    delet = input()
    if delet == "Так" or delet == "так":
       print("щоб вам видалити акаунт треба везти пароль")
       passw = input()
       if passw == password:
          del user['Stas']
          print("Ви видалили акаунт")
          
       else:
          print("Ви вели неправильний пароль")
    else:
       print("Слава Богу")
    
 elif user[log] == password:
  answ = ('Так', 'ні', 'Можливо', 'точно спробуй', 'сім раз відмірй і один відріж')
  point = 0
  print('Отримати відповідь? (Так/Ні)')
  word = input()
  while word == 'Так' or word == 'так':
   print(answ[random.randint(0, 4)])
   print()
   print("Отримати відповідь? (Так/Ні)")
   word = input()
   point += 1
   if point == 3:
    print("На сьогодні ти використав всі відповідь спробуй завтра")
    break
 else:
  print("Eror...")
elif sign == "2":

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
elif sign == "3":
 print("Щоб видалити акаунт ви маєте в ньго війти")
 print('Ведіть логін')
 log = input()
 print('Ведіть пароль')
 password = input()
 if user[log] == password:
  print("Тепер ви можети видалити акаунт")
  print("Ви точно хочете видалити акаунт? (Так/Ні)")
  delet = input()
 if delet == "Так" or delet == "так":
    del user['Stas']
    print("Ви видалили акаунт")
 else:
    print("Слава Богу")
  
else:
    print('ви вели неправиоьний пароль')
