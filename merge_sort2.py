lst = [4, 8 , 2 , 10, 1, 88, 0]

def merge_sort(lst):
    result = []

    if len(lst) < 2:
        return lst

    mid = len(lst)/2

    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result.extend(left)
    result.extend(right)

    return result

print merge_sort (lst)