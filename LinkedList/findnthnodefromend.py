#findnthnodefromend

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

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def nth_from_end(self, n):

        slow = self.head
        fast = self.head

        # Move fast n steps
        for _ in range(n):

            if fast is None:
                print("n is greater than length")
                return

            fast = fast.next

        # Move both pointers
        while fast is not None:

            slow = slow.next
            fast = fast.next

        print("Nth node from end =", slow.data)


ll = LinkedList()

ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)

ll.nth_from_end(2)