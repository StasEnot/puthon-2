import random
points_number = 0
print("Гра складається з 5-ти раундів")
print("В кожному раунді я загадую випадкове число від 1 до 5. Твоя задача його вгадати")
print("Якщо відповідь правельна, ти отримуєш 2 бали")
print("Якщо твоє число відрізняється на 1, ти отримуєш 1 бал")
for x in range(1,6):
    print("Раунд %s" %x)
    print("Ваша відповідь:")
    x =int(input())
    y = random.randint(1,5)
    print("Відповідь: %s" %y)

    if x == y:
        print("Ти отримаєш два бали")
        points_number += 2
        print()
    elif x - y == -1:
        print("Ти отримаєш один бал")
        points_number += 1
        print()
    elif x - y == -1:
        print("Ти отримаєш один бал")
        points_number += 1
        print()
    else :
        print("Ти нічого не отримуєш")
        print()

if points_number == 0 or points_number == 2 or points_number == 3:
    print("Повезе іншим разом,сума балів %s" %points_number)

elif points_number == 4 or points_number == 5 or points_number == 6:
    print("Непогано,сума балів = %s" %points_number)

elif points_number == 7 or points_number == 8 or points_number == 9 or points_number == 10:
    print("Ти молодець,сума балів %s" %points_number)
