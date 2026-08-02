class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    def reverse(self):

        prev = None
        curr = self.head

        while curr:

            next_node = curr.next

            curr.next = prev

            prev = curr

            curr = next_node

        self.head = prev

    def display(self):

        temp = self.head

        while temp:

            print(temp.data, end=" -> ")

            temp = temp.next

        print("None")


ll = LinkedList()

ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)

print("Before Reverse:")
ll.display()

ll.reverse()

print("After Reverse:")
ll.display()