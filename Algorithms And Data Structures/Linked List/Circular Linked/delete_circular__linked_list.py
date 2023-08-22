class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        if self.head is None:
            print("Empty Circular Linked List")
        else:
            temp = self.head
            print(temp.data, "-->", end=" ")
            while temp.next != self.head:
                temp = temp.next
                print(temp.data, "-->", end=" ")
            print(temp.next.data)

    def delete_begin(self):
        if self.head is None:
            print("No Node in Circular Linked List")
        else:
            if self.head == self.tail:
                self.head = None
            else:
                temp = self.head
                self.head = temp.next
                temp = None
                self.tail.next = self.head

    def delete_end(self):
        if self.head is None:
            print("No Node in Circular Linked List")
        else:
            if self.head == self.tail:
                self.head = None
            else:
                temp = self.head
                while temp.next != self.tail:
                    temp = temp.next
                self.tail = None
                self.tail = temp
                temp.next = self.head

    def delete_pos(self, pos):
        if self.head is None:
            print("No Node in Ciruclar Linked List")
        elif pos == 1:
            L.delete_begin()
        else:
            temp1 = self.head
            temp2 = self.head.next
            for i in range(1, pos-1):
                temp1 = temp1.next
                temp2 = temp2.next

            temp1.next = temp2.next
            if temp2 == self.tail:
                self.tail = temp1
                temp2 = None


L = CLL()

n1 = Node(10)
L.head = n1
L.tail = n1
L.tail.next = L.head
n2 = Node(20)
L.tail.next = n2
L.tail = n2
L.tail.next = L.head
n3 = Node(30)
L.tail.next = n3
L.tail = n3
L.tail.next = L.head
n4 = Node(40)
L.tail.next = n4
L.tail = n4
L.tail.next = L.head

# L.delete_begin()
# L.display()

# L.delete_begin()
# L.display()

# L.delete_end()
# L.display()

# L.delete_end()
# L.display()
L.delete_pos(4)
L.display()
