# 10 calculate the sum of odd numbers in the range of 1 to 10
i = 1
sum1 = 0
while i <= 10:
    if i % 2 == 1:
        sum1 += i
    i = i + 1
print(sum1)
