def list_length(lst):
    count = 0
    for i in lst:
        count += 1
    return count



def sort_list(lst):
    n = list_length(lst)

    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    return lst
lst = [1,4,6,4,3,76,22,31]
print("sorted list: ",sort_list(lst))