class Solution:

    def partition(self, head, x):

        small_dummy = ListNode(0)
        large_dummy = ListNode(0)

        small = small_dummy
        large = large_dummy

        while head:

            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next

            head = head.next

        large.next = None
        small.next = large_dummy.next

        return small_dummy.next
    
    //Time Complexity: O(n) where n is the number of nodes in the linked list. We traverse the list once.
    //Space Complexity: O(1) as we are not using any extra space.