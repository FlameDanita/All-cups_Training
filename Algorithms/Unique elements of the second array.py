if __name__ == "__main__":
    str_1 = input().split()
    n, m = str_1[0], str_1[1]

    arr_1 = list(map(int, input().split()))
    arr_2 = list(map(int, input().split()))

    arr_ans = []
    for elem_2 in arr_2:
        flag = False
        for elem_1 in arr_1:
            if elem_2 == elem_1:
                flag = True
                break

        if flag:
            arr_ans.append(elem_2)

    for elem in arr_ans:
        if elem in arr_2:
            arr_2.remove(elem)

    print(len(arr_2))
    print(*arr_2)
