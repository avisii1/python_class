# 11 check which sum is greater, odd or even number sum?
i = 1
even_sum = 0
odd_sum = 0
while i <= 10:
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
    i = i + 1
print("Even sum = ", even_sum)
print("Odd sum = ", odd_sum)
if even_sum > odd_sum:
    print("even sum is greatest")
else:
    print("odd sum is greatest")
