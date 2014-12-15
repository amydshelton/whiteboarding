"""You are in a room with a circle of 100 chairs. The chairs are numbered sequentially from 1 to 100.

At some point in time, the person in chair #1 will be asked to leave. The person in chair #2 will be skipped, and the person in chair #3 will be asked to leave. This pattern of skipping one person and asking the next to leave will keep going around the circle until there is one person left the survivor.

Write a program to determine which chair the survivor is sitting in."""



#### RECURSIVE WAY ###
ppl_in_chairs = []

for i in range(1,101):
    ppl_in_chairs.append(i)


def ask_ppl_to_leave(list_name):
    if len(list_name) == 1:
        print list_name[0]
    else:
        remaining_ppl = []
        for i in range(len(list_name)):
            if i % 2 == 1:
                remaining_ppl.append(list_name[i])
        ask_ppl_to_leave(remaining_ppl)

# ask_ppl_to_leave(ppl_in_chairs)


##### LINKED LIST WAY ###

from creating_linked_lists import LinkedList

ppl_in_chairs = LinkedList()

for i in range(1,101):
    ppl_in_chairs.AddNode(i)

# ppl_in_chairs.PrintList()

def ask_ppl_to_leave_ll(ll_name):
    next_elem = ll_name.head.next
    while next_elem != None:
        ll_name.head = next_elem
        print ll_name.head.data
        while next_elem != None:
            print next_elem.data

            next_elem.next = next_elem.next.next
            next_elem = next_elem.next
            print next_elem.next.data
    print ll_name.head.data

ask_ppl_to_leave_ll(ppl_in_chairs)
