import heapq


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, item) -> int:
        """
        Time - O(N)
        Space -
        """
        heapq.heappush(self.queue, item)

    def pop(self) -> int:
        """
        Time - O(1)
        Space - O(1)
        """
        if self.queue:
            return heapq.heappop(self.queue)

    def peek(self) -> int:
        """
        Time - O(1)
        Space - O(1)
        """
        if self.queue:
            return self.queue[0]
