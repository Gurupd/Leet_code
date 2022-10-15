# remove nth node from the end of linked list

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        left=dummy
        right=head
        # to move right pointer to nth node 
        while n>0 and right:
            right=right.next
            n=n-1
        # move left and right pointers
        while right:
            right=right.next
            left=left.next
        
        left.next=left.next.next
        return dummy.next