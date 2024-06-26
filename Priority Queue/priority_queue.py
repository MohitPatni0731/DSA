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
