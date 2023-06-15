# tuples
tup = (["avaishek", "ram"], "thor", "avengers", 1, 33)
# tup[1] = "jaari" # tuples are immutable
intermediate = tup[0][0].replace("a", "b")
tup[0][0] = intermediate
print(tup)

l1 = [['ram', 22, 75],
      ['shyam', 19, 77]]
print(l1)
l1.append(['hari', 18, 78])
print(l1)

# nested list
l1 = []
# l1 = list[]
n = int(input("enter the no of details: "))
for i in range(n):
    new_list = []
    name = input("enter your name: ")
    age = int(input("enter your age:"))
    marks = float(input("enter the obtained marks: "))
    new_list.append(name)
    new_list.append(age)
    new_list.append(marks)
    l1.append(new_list)
print(l1)

loc = r"c:\\users\\avishek"  # raw string
print(loc)
