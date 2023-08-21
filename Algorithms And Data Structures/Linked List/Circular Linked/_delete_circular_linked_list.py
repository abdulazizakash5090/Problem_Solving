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

    def add_begin(self, x):
        new = Node(x)
        if self.head is None:
            self.head = new
            self.tail = new
            self.tail.next = self.head
        else:
            new.next = self.head
            self.tail.next = new
            self.head = new

    def add_end(self, x):
        new = Node(x)
        if self.head is None:
            self.head = new
            self.tail = new
            self.tail.next = self.head
        else:
            self.tail.next = new
            self.tail = new
            self.tail.next = self.head

    def add_position(self, pos, x):
        new = Node(x)
        if self.head is None:
            self.head = new
            self.tail = new
            self.tail.next = self.head
        else:
            if pos == 1:
                L.add_begin(x)
            else:
                temp = self.head
                for i in range(1, pos-1):
                    temp = temp.next
                new.next = temp.next
                temp.next = new


L = CLL()
# L.display()

L.add_begin(10)
# L.display()
L.add_begin(20)
# L.display()
L.add_begin(30)
# L.display()

L.add_end(5)
# L.display()

L.add_end(1)
L.display()

L.add_position(3, 15)
L.display()

L.add_position(1, 40)
# n1 = Node(10)
# L.head = n1
# L.tail = n1
# L.tail.next = L.head
# L.display()
# print("After First node")


# n2 = Node(20)
# L.tail.next = n2
# L.tail = n2
# L.tail.next = L.head
# L.display()
# print("After second second node")

# n3 = Node(30)
# L.tail.next = n3
# L.tail = n3
# L.tail.next = L.head
# L.display()
# print("After Thired node")
