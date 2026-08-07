//linkedlist cycle
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

    # Create cycle
    def create_cycle(self):

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = self.head.next

    # Detect cycle
    def has_cycle(self):

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


ll = LinkedList()

ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)

ll.create_cycle()

if ll.has_cycle():
    print("Cycle Detected")
else:
    print("No Cycle")