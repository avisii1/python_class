# print("Welcome to movie mania!")
# ticket = 450
# popcorn = 350
# drinks = 150
# snacks = 250
# total = ticket + popcorn + drinks + snacks
# print("total amount is", total)
# paid_amount = 2000
# ret_amount = paid_amount - total
# print("returned amount is", ret_amount)
#
# pani = 1500
# batti = 1000
# rent = 10000
# phor = 120
# total = pani + batti + rent + phor
# print("total kharcha per year", total*12)
# print("total kharcha per month", total)

# shopping in shopping mall
# shirt = 1800
# pant = 3000
# shoes = 3000
# total = shirt + pant + shoes
# print("total amount is", total)
# paid_amount = 8000
# ret_amount = paid_amount - total
# print("returned amount is", paid_amount - total)


# total savings
# rent = 10000
# water = 500
# electricity = 1000
# internet = 1500
# others = 15000
# total_expenditures = rent + water + electricity + internet + others
# print("total expenditures is", total_expenditures)
# total_income = 50000
# print("total income is", total_income)
# print("total saving is", total_income - total_expenditures)
#
# print(2022, 2, 3, sep="-")
#
# name = input("Enter your name: ")  # type is always string
# print(name)

# num = input("enter an integer: ")
# print(type(num))
# num = int(num)
# print(type(num))
# print("integer is", num)
#
# a = 22
# print(id(a))  # id to check memory
# a = 44
# print(id(a))
# a = 55
# print(id(a))

# garbage collector

# class 4
# num1 = int(input("Enter first number: "))
# num2 = int(input("enter second number: "))
# num3 = int(input("enter third number: "))
# res = num1 + num2 + num3
# print("first number is", num1)
# print("Second number is", num2)
# print("third number is", num3)
# print("sum is ", res)

# conditional statement
# temp = float(input("Enter today's temperature: "))
# print("Today's temperature is", temp)
# if temp > 30:
#     print("its a hot day")
# if temp > 40:
#     print("It's too hot")

# age = int(input("enter your age: "))
# print("your age is", age)
# if age >= 18:
#     print("Eligible for voting")
#     if age >= 22:
#         print("eligible for marriage")
#     else:
#         print("not eligible for marriage")
# # if age < 18:
# #     print("Not eligible for voting")
# #     print("Future is there at your access")
# #     print("This is inside if statement")
# else:
#     print("Not eligible for voting")
# print("this is outside if statement")

# num = int(input("Enter any number: "))
# if num > 0:
#     print("this is positive number")
# else:
#     print("this is negative number")

# shirt = int(input("Enter the cost of shirt: "))
# pant = int(input("Enter the cost of pant: "))
# total_cost = shirt + pant
# print("your total cost is ", total_cost)
# paid_amount = int(input("Enter the amount to be paid: "))
# if paid_amount < total_cost:
#     print("your cost is higher than the paid amount, please pay again: ")
#     repaid = int(input("Enter additional amount: "))
#     total_payment = repaid + paid_amount
#     if total_payment < total_cost:
#         print("What is this behaviour bro?")
#         response = input("Do you want to pay or not?, Yes or No: ")
#         if response == "Yes":
#             repaid_again = int(input("repaid amount again: "))
#             total_payment = total_payment + repaid_again
#             if total_payment < total_cost:
#                 print("Insufficient payment")
#             else:
#                 if total_payment == total_cost:
#                     print("Thank you for shopping with us")
#                 else:
#                     change_returned = total_payment - total_cost
#                     print("return change = " + str(change_returned), end="\n" + "Thank you for shopping with us")
#         if response == "No":
#             print("please kindly get out from this shop")
#     else:
#         if total_payment == total_cost:
#             print("Thank you for shopping with us")
#         else:
#             change_returned = total_payment - total_cost
#             print("return change = " + str(change_returned), end="\n" + "Thank you for shopping with us")
# else:
#     if paid_amount == total_cost:
#         print("Thank you for shopping with us")
#     else:
#         change_returned = paid_amount - total_cost
#         print("return change = " + str(change_returned), end="\n" + "Thank you for shopping with us")

# age = int(input("Enter your age: "))
# print("Entered age is", age)
# if 0 < age <= 130:  # age > 0 and age <= 130
#     if age >= 18:
#         print("eligible for voting")
#     else:
#         print("Not eligible for voting")
# else:
#     print("Invalid input")

# fname, lname, address= input("Enter your first name, last name and address: ").split()
# print(fname, lname, "Lives in ", address)

# mark1 = mark2 = mark3 = 55
# print(mark1, mark2, mark3)

mark1 = float(input("Enter the mark1: "))
mark2 = float(input("Enter the mark2: "))
mark3 = float(input("Enter the mark3: "))
if mark1 < 32 or mark2 < 32 or mark3 < 32:
    if mark1 < 0 or mark2 < 0 or mark3 < 0:
        print("wrong input!!!")
    else:
        print("You failed")
elif mark1 > 100 or mark2 > 100 or mark3 > 100:
    print("Wrong input")
else:
    total = mark1 + mark2 + mark3
    per = total / 3
    if per > 80:
        print("Distinction, percentage = ", per)
    elif per > 60:
        print("First Division, percentage = ", per)
    else:
        print("Third division, percentage = ", per)


