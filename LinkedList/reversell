class Node {

    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {

    Node head;

    void insert(int data) {

        Node newNode = new Node(data);

        if (head == null) {
            head = newNode;
            return;
        }

        Node temp = head;

        while (temp.next != null)
            temp = temp.next;

        temp.next = newNode;
    }

    void reverse() {

        Node prev = null;
        Node curr = head;
        Node next = null;

        while (curr != null) {

            next = curr.next;     // Save next node

            curr.next = prev;     // Reverse link

            prev = curr;          // Move prev

            curr = next;          // Move curr
        }

        head = prev;
    }

    void display() {

        Node temp = head;

        while (temp != null) {

            System.out.print(temp.data + " -> ");

            temp = temp.next;
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
        list.insert(40);
        list.insert(50);

        System.out.println("Before Reverse:");

        list.display();

        list.reverse();

        System.out.println("After Reverse:");

        list.display();
    }
}