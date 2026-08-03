class Solution {

    public ListNode rotatelist(ListNode head, int k) {

        if (head == null || head.next == null || k == 0)
            return head;

        // Find length
        ListNode temp = head;
        int length = 1;

        while (temp.next != null) {
            temp = temp.next;
            length++;
        }

        // Make circular
        temp.next = head;

        // Effective rotation
        k = k % length;

        // Find new tail
        int steps = length - k - 1;

        ListNode newTail = head;

        for (int i = 0; i < steps; i++) {
            newTail = newTail.next;
        }

        // New head
        ListNode newHead = newTail.next;

        // Break circle
        newTail.next = null;

        return newHead;
    }
}