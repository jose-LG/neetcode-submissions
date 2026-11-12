class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #if not head or not head.next:
           # return head #size of zero or one

        prev = None
        currNode = head 

        while currNode:
            temp = currNode.next
            currNode.next = prev
            prev = currNode
            currNode = temp
        return prev