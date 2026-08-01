class Solution:
    def removeNthFromEnd(self, head, n):

        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Move fast n+1 steps
        for _ in range(n + 1):
            fast = fast.next

        # Move both
        while fast:

            slow = slow.next
            fast = fast.next

        # Delete
        slow.next = slow.next.next

        return dummy.next