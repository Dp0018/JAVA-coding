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


    void nthNodeFromEnd(int n) {
        if (head == null) {
            System.out.println("The linked list is empty.");
            return;
        }

        Node fast = head;
        Node slow = head;

        // Move the fast pointer n nodes ahead
        for (int i = 0; i < n; i++) {
            if (fast == null) {
                System.out.println("The linked list has fewer than " + n + " nodes.");
                return;
            }
            fast = fast.next;
        }

        // Move both pointers until the fast pointer reaches the end
        while (fast != null) {
            fast = fast.next;
            slow = slow.next;
        }

        System.out.println("The " + n + "th node from the end is: " + slow.data);
    }

}