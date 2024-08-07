class PriorityQueue:
    def __init__(self, is_min_heap=True):
        """
        Time - O(1)
        Space - O(1)
        """
        self.queue = []
        self.is_min_heap = is_min_heap

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

    def peek(self) -> int | None:
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

    def heapifyUp(self, i) -> None:
        """
        Time - O(N)
        Space - O(1)
        """
        while i > 0 and self.queue[self.parent(i)] < self.queue[i]:
            p = self.parent(i)
            self.queue[i], self.queue[p] = self.queue[p], self.queue[i]
            i = p

    def heapifyDown(self, i) -> None:
        """
        Time - O(N)
        Space - O(1)
        """
        left = self.leftChild(i)
        right = self.rightChild(i)
        largest = i
        while self.queue:
            if left and self.queue[left] > self.queue[largest]:
                largest = left

            if right and self.queue[right] > self.queue[largest]:
                largest = right

            if largest != i:
                self.queue[i], self.queue[largest] = self.queue[largest], self.queue[i]
            else:
                break

    def insert(self, item) -> None:
        """
        Time - O(N)
        Space - O(1)
        """
        self.queue.append(item)
        if self.is_min_heap:
            self.heapifyUp(len(self.queue) - 1)
        else:
            self.heapifyDown(len(self.queue) - 1)

    def print_queue(self) -> None:
        """
        Time - O(N)
        Space - O(1)
        """
        return self.queue
