class PriorityQueue:
    def __init__(self):
        """
        Time - O(1)
        Space - O(1)
        """
        self.queue = []

    def parent(self, i) -> int:
        """
        Time - O(1)
        Space - O(1)
        """
        return (i - 1) // 2

    def leftChild(self, i) -> int:
        """
        Time - O(1)
        Space - O(1)
        """
        return (2 * i) + 1

    def rightChild(self, i) -> int:
        """
        Time - O(1)
        Space - O(1)
        """
        return (2 * i) + 2

    def peek(self) -> int:
        """
        Time - O(1)
        Space - O(1)
        """
        return self.queue[0] if self.queue else None

    def isEmpty(self) -> bool:
        """
        Time - O(1)
        Space - O(1)
        """
        return len(self.queue) == 0

    def heapify(self, i) -> None:
        """
        Time - O(N)
        Space - O(N)
        """
        while i > 0 and self.queue[self.parent(i)] < self.queue[i]:
            p = self.parent(i)
            self.queue[i], self.queue[p] = self.queue[p], self.queue[i]

    def insert(self, item) -> int:
        """
        Time - O(N)
        Space - O(N)
        """
        self.queue.append(item)
        self.heapifyUp(self.queue)

    def print_queue(self) -> None:
        """
        Time - O(N)
        Space - O(N)
        """
        return self.queue
