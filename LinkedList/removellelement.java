class Solution {

    public ListNode removeElements(ListNode head, int val) {

        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode prev = dummy;
        ListNode curr = head;

        while (curr != null) {

            if (curr.val == val) {

                // Remove current node
                prev.next = curr.next;

            } else {

                // Move prev only if node is kept
                prev = curr;
            }

            curr = curr.next;
        }

        return dummy.next;
    }
}