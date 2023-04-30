year = int(input("Введите год: "))
#
#Без тернарного оператора

if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
    print("Год " + str(year) + " високосный")
else:
    print("Год " + str(year) + " не високосный")

#С использованием тернарного оператора
# var = print("Год високосный") if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0) else print("Год не високосный")