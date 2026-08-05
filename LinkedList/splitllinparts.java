class Solution {
    public ListNode[] splitListToParts(ListNode head, int k) {
        int length = 0;
        ListNode curr = head;
        while(curr!=null){
            length++;
            curr = curr.next;
        }
        int partSize = length/k;

        int extra = length%k;

        curr=head;
        for(int i=0;i<k;i++){
            result[i] = curr;
            int currentPartSize = partSize;

            if(extra>0){
              currentPartSize++;
              extra--;  
            }

             for (int j = 1; j < currentPartSize && curr != null; j++) {
                curr = curr.next;
            }

            /
            if (curr != null) {

                ListNode nextPart = curr.next;

                curr.next = null;

                curr = nextPart;
            }
        } return result;



        
    }
}