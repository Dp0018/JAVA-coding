class Node{
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

     // Find the middle element of the linked list
     public int findMiddleElement(){
         if(head == null){
             throw new IllegalStateException("The linked list is empty.");
         }
         Node slowPointer = head;
         Node fastPointer = head;

         while(fastPointer != null && fastPointer.next != null){
             slowPointer = slowPointer.next;
             fastPointer = fastPointer.next.next;
         }
         return slowPointer.data;
     }

}
public class Main {

    public static void main(String[] args) {

        LinkedList list = new LinkedList();

        list.insert(10);
        list.insert(20);
        list.insert(30);
        list.insert(40);
        list.insert(50);

        list.middle();
    }
}