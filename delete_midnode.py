
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=left=head
        count=0
        dummy=ListNode(0,head)
        
        if head.next is None:
            print("[]")
        else :
            while cur:
                cur=cur.next
                count=count+1
                mid=count//2
            # print(mid)
            
            left=head
            right=head 
            while mid>0 and right is not None:
                left=right
                right=right.next
                mid=mid-1
            left.next=left.next.next
            return dummy.next
       
       