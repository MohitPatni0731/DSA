class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, item) -> int:
        """
        Time - O(N)
        Space - O(N)
        """
        if self.queue is None:
            self.queue.append(item)
        else:
            for i in range(len(self.queue)):
                if self.queue[i] > item:
                    self.queue.insert(i, item)
                    break
            self.queue.append(item)

    def pop(self) -> int:
        """
        Time - O(1)
        Space - O(1)
        """
        if self.queue:
            return self.queue.pop(0)

    def peek(self) -> int:
        """
        Time - O(1)
        Space - O(1)
        """
        if self.queue:
            return self.queue[0]
