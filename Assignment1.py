# 1 to generate multiplication table from 1 to 10
i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(str(i) + "*" + str(j) + " = ", i*j)
        j = j + 1
    print("\t \t")
    i = i + 1
