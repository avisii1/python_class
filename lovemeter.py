boy_name = input("Enter the name of a boy: ")
girl_name = input("Enter the name of a girl: ")
boy_len = len(boy_name)
girl_len = len(girl_name)
diff = abs(boy_len - girl_len)
if boy_len == girl_len:
    print("percentage = 100%")
elif boy_name[0] == girl_name[0]:
    print("percentage = 100%")
else:
    if diff >= 3:
        print("percentage = 70%")
    else:
        print("percentage = 80%")
