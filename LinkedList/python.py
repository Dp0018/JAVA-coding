class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # Find the length of the linked list
    def length(self):
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        return count

    # Display the linked list
    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main Program
if __name__ == "__main__":

    ll = LinkedList()

    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    ll.insert(40)

    print("Linked List:")
    ll.display()

    print("Length of Linked List =", ll.length())