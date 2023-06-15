# try:
#     f_age = 22
#     s_age = 33
#     if f_age < s_age:
#         raise Exception("check the age of father and son")
# except Exception as ex:
#     print(ex)
# else:
#     print(f"father age is {f_age} and son age is {s_age}")
# finally:
#     print("age handler")
# print("out of exception handling")

# f = open("test.txt")
# data = f.read()
# print(data)
# print("Now need to store")
# f1 = open("test.txt", 'a')
# data = f1.write("\n some test contents")
# f2 = open("test.txt")
# data = f2.read()
# print(data)


# with open('test.txt') as f:  # automatically closes file
#     data = f.read()
#     print(f.mode)  # kun chai mode ma open gareko
#     print(f.name)  # file ko name
#     print(data)
# print(f.closed)  # checking whether file is closed or not

# working with csv file
import csv
with open('details.csv') as f:
    data = csv.reader(f)
    # print(data)  # prints object memory address
    next(f)  # removes headings such as sn, name , age and others
    for i in data:  # to access the data from that object
        print(i)
        # print(i[0:3])  # slicing of details

# to write in csv file
with open('details.csv','w') as f:
    data = csv.writer(f)
    data.writerow(7, 'avishek', 22, 44, 'ktm')
