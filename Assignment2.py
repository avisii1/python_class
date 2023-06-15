# 2 ask user for the range of table
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
while start <= end:
    j = 1
    while j <= 10:
        print(str(start) + "*" + str(j) + " = ", start*j)
        j = j + 1
    print("\t \t")
    start = start + 1
