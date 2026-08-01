## LinkedList

##1. Insert At Beginning(java)

public void addFirst(string data) {

    Node newNode = new Node(data);

    if (head==null){
        head = newNode
    }

    newNode.next = head;
    haed = newNode
}


(python)

def insert_at_beginning(self, data):
    new_node = Node(data).   # Create a new node
    new_node.next = self.head. # New node points to current head
    self.head = new_node.      # Head becomes the new node

