num = int(input("Enter the number: "))
name = input("Enter your name: ")
result = 1
for i in range(1, num + 1):
    result *= i
print(f"factorial of {num} asked by {name} is {result}")  # string formatting
