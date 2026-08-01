class Solution {

    public ListNode removeNthFromEnd(ListNode head, int n) {

        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode slow = dummy;
        ListNode fast = dummy;

        // Move fast n+1 steps
        for (int i = 0; i <= n; i++) {
            fast = fast.next;
        }

        // Move both pointers
        while (fast != null) {
            slow = slow.next;
            fast = fast.next;
        }

        // Delete node
        slow.next = slow.next.next;

        return dummy.next;
    }
}



"I use a dummy node to simplify edge cases, especially when the head needs to be removed. I keep two pointers, fast and slow, both starting at the dummy node. I first move fast n + 1 steps ahead so there's a fixed gap between them. Then I move both pointers together until fast reaches the end. At that point, slow is just before the node to remove, so I bypass it by setting slow.next = slow.next.next. This solution runs in O(n) time and uses O(1) extra space."