lst = [4,6,2,9,10,5,1]

def split_lst_up(lst):
    if len(lst) > 1:
        mid = len(lst)/2
        split_lst_up(lst[mid:])
        split_lst_up(lst[:mid])

    else:
        print lst
        return lst

# split_lst_up(lst)

# lst1 = [0,2,5]
# lst2 = [3,6,8]

def merge_sort(lst1, lst2):
    result_lst = []
    while len(lst1) > 0 and len(lst2) > 0:
        if lst1[0] < lst2[0]:
            result_lst.append(lst1.pop(0))
        else:
            result_lst.append(lst2.pop(0))

    result_lst.extend(lst1)
    result_lst.extend(lst2)

    return result_lst

# print merge_sort(lst1, lst2)

#stolen from the interwebs
def actually_merge_sort(lst):
    result = []
    if len(lst) < 2:
        return lst
    mid = int(len(lst)/2)
    y = actually_merge_sort(lst[:mid])
    z = actually_merge_sort(lst[mid:])
    while (len(y) > 0) or (len(z) > 0):
        if len(y) > 0 and len(z) > 0:
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        elif len(z) > 0:
            for i in z:
                result.append(i)
                z.pop(0)
        else:
            for i in y:
                result.append(i)
                y.pop(0)
    return result

print actually_merge_sort(lst)