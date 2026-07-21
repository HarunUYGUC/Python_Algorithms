# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        current = head

        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        
        return prev

# Example usage:
head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)

# Run the reverseList function
solution = Solution()
new_head = solution.reverseList(head)

# Print the reversed linked list
current = new_head
while current:
    print(current.val, end=" ")
    current = current.next
