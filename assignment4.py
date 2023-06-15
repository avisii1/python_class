# 4 find the largest number among entered two numbers
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
if num1 > num2:
    print(str(num1) + " is greater than " + str(num2))
else:
    print(str(num2) + " is greater than " + str(num1))