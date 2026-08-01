class Node :
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList :
    def __init__(self):
        self.head = None
        
    def middle(self):
        slow = self.head
        fast = self.head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            print("Middle element is:", slow.data)
            
ll = LinkedList()
ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(4)
ll.head.next.next.next.next = Node(5)
ll.middle()