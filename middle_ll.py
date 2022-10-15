# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start=head
        count=0
        while start is not None:
            count +=1
            start =start.next
        mid=count//2
        counter=0
        new=head
        while new is not None :
            if counter==mid:
                return new
            else:
                counter =counter+1
                new=new.next