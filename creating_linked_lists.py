class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def AddNode(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node

        if self.tail != None:
            self.tail.next = new_node

        self.tail = new_node

    def PrintList(self):
        node = self.head

        while node != None:
            print node.data,
            node = node.next

    def Length_of_List(self):
        current = self.head
        counter = 0
        while current:
            current = current.next
            counter +=1
        return counter


    def Reverse(self): 
        curr = self.head
        prev = None
        while curr is not None:
            gonna_go_there_next = curr.next # memorizing where I'm gonna go next
            curr.next = prev # change pointer direction, which i can do b/c i've already memorized where i'm going
            prev = curr # set where i am to be the newest previous  
            curr = gonna_go_there_next # go to the next one

        # reset head and tail properties appropriately
        old_head = self.head 
        self.head = self.tail
        self.tail = old_head

        return self

    def Insert_Node(self, insertion_point, insertion_value):
        inserted_node = Node(insertion_value)
        if insertion_point == 0:
            old_head = self.head
            new_head = inserted_node
            new_head.next = old_head
            self.head = new_head
        else:
            where_we_are_now = self.head
            count = 1
            while count < insertion_point and where_we_are_now.next:
                where_we_are_now = where_we_are_now.next
                count +=1
            inserted_node.next = where_we_are_now.next
            where_we_are_now.next = inserted_node
        return self

    def Get_Node(self, index):
        current = self.head
        counter = 0
        if not current:
            return "List isn't that long!"
        while counter < index:
            if not current:
                return "List isn't that long!"
            else:
                current = current.next
                counter += 1

        return current.data

    def Get_Index(self, value):
        current = self.head
        counter = 0
        while value != current.data:
            current = current.next
            counter += 1
            if not current:
                return "Can't find it!"
        return counter

    def Delete_Node_at_Index(self, index):
        current = self.head
        counter = 0
        if not current:
            return "List isn't that long!"
        while counter < index:
            if not current:
                return "List isn't that long!"
            previous = current
            current = current.next
            counter += 1
        previous.next = current.next
        return "Deleted"

    def Minimum(self):
        current = self.head
        minimum = current.data
        for i in range(self.Length_of_List()):
            if current.data < minimum:
                minimum = current.data
            current = current.next
        return minimum

    def Maximum(self):
        current = self.head
        maximum = current.data
        for i in range(self.Length_of_List()):
            if current.data > maximum:
                maximum = current.data
            current = current.next
        return maximum



# A-> B-> C-> D-> none
def reverse_recursive(node, previous):
    if node == None:
        print previous.data
    gonna_go_there_next = node.next # memorize where we're going to go
    node.next = previous #switch pointer
    print reverse_recursive(gonna_go_there_next, node)



lst = LinkedList()
lst.AddNode(0)
lst.AddNode(1)
lst.AddNode(2)
lst.AddNode(3)


lst.PrintList()