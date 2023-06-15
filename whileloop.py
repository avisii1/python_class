# a = 1
# while a <= 10:
#     print(a, end=" ")
#     a = a + 1


# a = int(input("Enter any number: "))
# num = int(input("Enter stopping criteria: "))
# update = int(input("Enter number to update:"))
# while a <= num:
#     print(a, end=" ")
#     a = a + update

# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter second number:"))
# if num1 > num2:
#     print(str(num1) + " is larger than " + str(num2))
# elif num1 == num2:
#     print("Both are equal")
# else:
#     print(str(num2) + " is larger than " + str(num1))

# name = input("Enter your name: ")
# for x in name:
#     if x.isdigit():
#         print("Invalid input")
#         break
#     else:
#         print(name)

# shirt = int(input("Enter the cost of shirt: "))
# pant = int(input("Enter the cost of pant: "))
# total_cost = shirt + pant
# print("your total cost is ", total_cost)
# paid_amount = int(input("Enter the amount to be paid: "))
# while paid_amount < total_cost:
#     difference = total_cost - paid_amount
#     print("Insufficient amount, please pay" + str(difference) + "more")
#     repaid = int(input("Enter additional amount: "))
#     paid_amount = paid_amount + repaid
# if paid_amount > total_cost:
#     print("return change = ", paid_amount - total_cost)
#     print("Thank you for shopping with us")
# else:
#     print("Thank you for shopping with us")

# i = 1
# while i <= 5:
#     print("Enter marks of " + str(i) + " student: ")
#     mark1 = float(input("Enter the mark1: "))
#     mark2 = float(input("Enter the mark2: "))
#     mark3 = float(input("Enter the mark3: "))
#     if mark1 < 32 or mark2 < 32 or mark3 < 32:
#         if mark1 < 0 or mark2 < 0 or mark3 < 0:
#             print("wrong input!!!")
#         else:
#             print("You failed")
#     elif mark1 > 100 or mark2 > 100 or mark3 > 100:
#         print("Wrong input")
#     else:
#         total = mark1 + mark2 + mark3
#         per = total / 3
#         if per > 80:
#             print("Distinction, percentage = ", per)
#         elif per > 60:
#             print("First Division, percentage = ", per)
#         else:
#             print("Third division, percentage = ", per)
#     i = i + 1

i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(str(i) + "*" + str(j) + " = ", i*j)
        j = j + 1
    i = i + 1
