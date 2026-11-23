from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.total = 0
        self.count = 0
        self.size = size

    def next(self, val: int) -> float:
        while self.count >= self.size:
            popped = self.queue.popleft()
            self.total -= popped
            self.count -= 1
        
        self.total += val
        self.count += 1
        self.queue.append(val)

        return float(self.total/self.count)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
