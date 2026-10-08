class Solution:

    def removeElements(self, head, val):

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:

            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next

        return dummy.next
    
    // Time Complexity: O(n) where n is the number of nodes in the linked list. We traverse the list once.
    // Space Complexity: O(1) as we are not using any extra space.