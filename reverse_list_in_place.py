lst = [0,1,2,3,4]

def reverse_list_in_place(lst):
    end_traverser = -1
    beginning_traverser = 0
    for i in range(len(lst)/2):
        temp = lst[end_traverser]
        lst[end_traverser] = lst[beginning_traverser]
        lst[beginning_traverser] = temp
        end_traverser = end_traverser - 1
        beginning_traverser = beginning_traverser + 1

    print lst

reverse_list_in_place(lst)
