class Solution:

    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)
        tail = dummy

        carry = 0

        while l1 or l2 or carry:

            total = carry

            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next

            carry = total // 10

            tail.next = ListNode(total % 10)

            tail = tail.next

        return dummy.next
    
    //time complexity: O(max(n, m)) where n and m are the lengths of the two linked lists
    //space complexity: O(max(n, m)) for the new linked list created to store