# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
n = int(input("Введите количество рядов: "))
m = int(input("Введите количество колонок: "))
k = int(input("Введите количество долек, которое необходимо отломить: "))

if k > n*m:
    print("Невозможно отломить указанное количество долек")
else:
    if k % n == 0 or k % m == 0:
        print("Да, можно отломить указанное количество долек")
    else:
        print("Нет, невозможно отломить указанное количество долек")