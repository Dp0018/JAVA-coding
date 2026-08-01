 class Node(){
    int data;
    Node next;

    public Node(int data){
        this.data = data;
        this.next = null;
    }
}

class LinkedList{
    Node head;

    //Insert at the end of the linked list
    void insert(int data){
        Node newNode = new Node(data);
        if(head == null){
            head = newNode;
            return;

        } 
        Node current = head;
        while(current.next != null){
            current = current.next; 
          }
          current.next = newNode;

}

     // Find the length of the linked list
     public int length(){
         int count = 0;
         Node current = head;
         while(current != null){
             count++;
             current = current.next;
         }
         return count;
     }

     //display the linked list
     public void display(){
         Node current = head;
         while(current != null){
             System.out.print(current.data + " -> ");
             current = current.next;
         }
         System.out.println("null");
     }

}

public class Main {
    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        list.insert(10);
        list.insert(20);
        list.insert(30);
        list.display(); // Output: 10 -> 20 -> 30 -> null
        System.out.println("Length of the linked list: " + list.length()); // Output: Length of the linked list: 3
    }
}