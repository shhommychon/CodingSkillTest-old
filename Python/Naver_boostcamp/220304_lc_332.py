### LeetCode
### 332. Reconstruct Itinerary https://leetcode.com/problems/reconstruct-itinerary/
### <파이썬 알고리즘 인터뷰> 38. 일정 재구성

from typing import List
from collections import defaultdict

class Solution:
    def __init__(self):
        self.answer = list()
    
    def dfs(self, current: str):
        if len(self.ticket_dict[current]) == 0:
            self.answer.append(current)
            return
        
        while self.ticket_dict[current]:
            next_visit = self.ticket_dict[current].pop()
            self.dfs(next_visit)
        
        self.answer.append(current)
        return


    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticket_dict = defaultdict(list)
        for t in tickets:
            ticket_dict[t[0]].append(t[1])
        for t in ticket_dict:
            ticket_dict[t].sort(reverse=True)

        self.ticket_dict = ticket_dict
        
        self.dfs("JFK")
        
        return self.answer[::-1]
