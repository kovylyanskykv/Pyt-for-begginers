year = int(input("Введите год:"))


if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
    print("Год високосный")
else:
    print("Год не високосный")
