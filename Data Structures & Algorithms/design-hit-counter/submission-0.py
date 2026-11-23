from collections import deque
class HitCounter:

    def __init__(self):
        self.hits = deque()
        self.counter = 0

    def hit(self, timestamp: int) -> None:
        
        self.hits.append(timestamp)
        self.counter += 1

    def getHits(self, timestamp: int) -> int:
        while self.hits and timestamp - 300 >= self.hits[0]:
            self.hits.popleft()
            self.counter -= 1
        return self.counter


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
