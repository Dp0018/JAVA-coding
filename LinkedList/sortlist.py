class Solution:

    def sortList(self, head):

        if head is None or head.next is None:
            return head

        # Find middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split
        second = slow.next
        slow.next = None

        # Sort recursively
        left = self.sortList(head)
        right = self.sortList(second)

        # Merge
        return self.merge(left, right)

    def merge(self, l1, l2):

        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:

            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        if l1:
            tail.next = l1

        if l2:
            tail.next = l2

        return dummy.next
    //Time Complexity: O(n log n) where n is the number of nodes in the linked list. We are dividing the list into halves and merging them back.
    //Space Complexity: O(log n) due to recursive stack space used for sorting the linked