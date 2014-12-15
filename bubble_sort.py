lst = [2,5,1,4,10,7]

#assumes no dupes

def bubble_sort(lst):
    totes_sorted = False
    length_of_list = len(lst)
    while totes_sorted == False:
        count_of_test_passed = 0
        for i in range(length_of_list):
            if i == length_of_list - 1:
                continue
            else:
                if lst[i] > lst[i+1]:
                    temp = lst[i+1]
                    lst[i+1] = lst[i]
                    lst[i] = temp
                else:
                    count_of_test_passed +=1
                    if count_of_test_passed == length_of_list - 1:
                        totes_sorted = True
    return lst

print bubble_sort(lst)

def better_bubble_sort(lst):
    is_sorted = False

    while is_sorted == False:
        is_sorted = True

        for i in range(len(lst)-1):
            num1, num2 = lst[i], lst[i+1]

            if num1 > num2:
                is_sorted = False
                lst[i], lst[i + 1] = num2, num1

    return lst

print better_bubble_sort(lst)

def even_better_bubble_sort(lst):
    is_sorted = False
    len_of_lst_to_check = len(lst) - 1
    while is_sorted == False:
        is_sorted = True

        for i in range(len_of_lst_to_check):
            num1, num2 = lst[i], lst[i+1]

            if num1 > num2:
                is_sorted = False
                lst[i], lst[i + 1] = num2, num1

        len_of_lst_to_check -= 1

    return lst

print even_better_bubble_sort(lst)