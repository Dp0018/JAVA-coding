class Solution:

    def rotateRight(self, head, k):

        if head is None or head.next is None or k == 0:
            return head

        # Find length
        length = 1
        temp = head

        while temp.next:
            temp = temp.next
            length += 1

        # Make circular
        temp.next = head

        # Effective rotation
        k %= length

        # Find new tail
        steps = length - k - 1

        new_tail = head

        for _ in range(steps):
            new_tail = new_tail.next

        new_head = new_tail.next

        # Break circle
        new_tail.next = None

        return new_head