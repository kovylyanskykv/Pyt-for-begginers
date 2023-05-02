rating = [7, 5, 3, 3, 2]
print(*rating, sep=', ')
number = int(input("Введите целое число: "))
while number != "":
    rating.append(number)
    rating.sort(reverse=True)
    print(*rating, sep= ", ")
    number = int(input("Введите целое число: "))
else:
    print(rating)
    print("Вы закончили цикл.")