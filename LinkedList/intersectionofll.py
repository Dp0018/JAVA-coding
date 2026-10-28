class Solution:

    def getIntersectionNode(self, headA, headB):

        p1 = headA
        p2 = headB

        while p1 != p2:

            p1 = headB if p1 is None else p1.next

            p2 = headA if p2 is None else p2.next

        return p1
    
    //time complexity: O(n + m) where n and m are the lengths of the two linked lists
    //space complexity: O(1) since we are using only two pointers and no additional data structures
    //This solution works by using two pointers, p1 and p2, which traverse the two linked lists. When one pointer reaches the end of its list, it is redirected to the head of the other list. This way, both pointers will traverse the same number of nodes when they meet at the intersection point or reach the end of both lists (None).   
    