# 4 find the largest number among entered three numbers
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
num3 = int(input("enter the third number: "))
if num1 > num2 and num1 > num3:
    print(str(num1) + " is greatest ")
elif num2 > num1 and num2 > num3:
    print(str(num2) + " is greatest ")
else:
    print(str(num3) + " is greatest ")
