# f = open("test.txt")
# f.close()
# print("this is remaining works")

# try except else finally
# try:
#     a = 22/0
#     print(a)
# except ZeroDivisionError as ze:
#     print(f"This is error {ze}")
# print("this is demo")

# try:
#     a = [1, 2, 3]
#     print(a[5])
#     # f = open("test.txt")
#     # f.close()
# except Exception as ex:  # problem aafei patta lagauxa
#     print(f"This is error {ex}")
# else:
#     print("we are on next stuff")
# finally:
#     print("this is try except block")
# print("this is demo")

try:
    # f = open("test1.txt", 'w') # write mode automatically creates file if it does not exist but replace  previous
    # contents
    # f = open("test1.txt", 'w') # x for creating
    # f = open("test1.txt", 'a')  # append mode automatically creates file if it does not exist and appends on  previous
    f = open("test.txt", 'r')
    # data = f.read()  # reads as string
    # data = f.readline()  # reads single line
    data = f.readlines()  # reads as list and supports indexing and other lists functions
    print(data)
    print(data[1])
    # contents
    f.close()
except Exception as ex:
    print(f"Error: {ex}")
else:
    print("Inside file")
print("This is remaining works")