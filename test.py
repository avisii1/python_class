def list_test(some_list):
    # print(some_list)
    # print(max(some_list))
    max_num = some_list[0]
    for i in some_list:
        if max_num < i:
            max_num = i
    print(f"largest number is {max_num}")


list_test([1, 2, 3, 4])
