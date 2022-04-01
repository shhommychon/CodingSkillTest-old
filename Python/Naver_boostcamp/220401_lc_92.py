### LeetCode
### 92. Reverse Linked List II https://leetcode.com/problems/reverse-linked-list-ii/
### <파이썬 알고리즘 인터뷰> 19. 역순 연결 리스트 II

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        new_head = []
        new_rev_mid = []
        new_tail = []
        
        count = 1
        while True:
            if count < left:
                new_head.append(head.val)
            elif left <= count <= right:
                new_rev_mid.append(head.val)
            else: # count > right:
                new_tail.append(head.val)
            if head.next is None:
                break
            else:
                head = head.next
                count+=1
        
        answer = None
        for val in new_tail[::-1] + new_rev_mid + new_head[::-1]:
            if answer is None:
                answer = ListNode(val)
            else:
                answer = ListNode(val, next=answer)
        
        return answer
