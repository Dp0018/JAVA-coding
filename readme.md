## LinkedList

##1. Insert At Beginning(java)

public void addFirst(string data) {

    Node newNode = new Node(data);

    if (head==null){
        head = newNode;
        return;
    }

    newNode.next = head;
    haed = newNode
}


(python)

def insert_at_beginning(self, data):
    new_node = Node(data).   # Create a new node
    new_node.next = self.head. # New node points to current head
    self.head = new_node.      # Head becomes the new node




##2.Insert AT Last

public void addLast(string data){
    node newNode = new Node(data);

    if(head == null){
        head = newNode;
        return;
    }

    Node currNode = head;
    while(currNode != null){
        currNode = currNode.next;
    }

    currNode.next = newNode;

}


(python)

def insert_at_last(self,data):
    new_node = Node(data)

    # If the linked list is empty
    if self.head is None:
       self.head = new_node
       return

     # Traverse to the last node
     temp = self.head

     while temp.next is not None:
        temp = temp.next

    # Link the last node to the new node

    temp.next = new_node



    

