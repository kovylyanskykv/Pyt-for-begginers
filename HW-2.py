num = str(input("Введите число:"))
sum_num1 = int(num[0:1])
sum_num2 = int(num[1:2])
sum_num3 = int(num[2:3])
sum = sum_num1 + sum_num2 + sum_num3
print(str(num) + " >>> Сумма числа " + str(num) + " равна " + str(sum))


#Могу ли я преобразовывать sum_num в int?
# sum = str(int(num[1:1]) + int(num[1:2]) + int(num[1:3]))