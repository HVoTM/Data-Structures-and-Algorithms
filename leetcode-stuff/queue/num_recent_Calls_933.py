from collections import deque
# LEETCODE 933. Number of Recent Calls
# Topic: Design, Deque, Data Stream

class RecentCounter:
    def __init__(self):
        self.rangemax = 0
        self.rangemin = 0
        self.requests = deque()

    def ping(self, t: int) -> int:
        # Since we are guaranteed that ping will always be larger than the previous calls
        self.rangemax = t
        self.requests.append(t)
        while self.requests[0] < self.rangemax - 3000:
            self.requests.popleft()
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)