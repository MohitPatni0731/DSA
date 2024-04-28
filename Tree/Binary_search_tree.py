from typing import Any
from typing import List


class BST:
    def __init__(self, data: Any) -> None:
        """
        Time - O(1)
        Space - O(1)
        """
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data: Any) -> None:
        """
        Time - O(N)
        Space - O(N)
        """
        if self is None:
            self.root = BST(data)

        if data < self.data:
            if self.left == None:
                self.left = BST(data)
            else:
                self.left.insert(data)
        else:
            if self.right == None:
                self.right = BST(data)
            else:
                self.right.insert(data)

    def preorder(self) -> List[Any]:
        """
        Time - O(N)
        Space - O(N)
        """
        preorder = []
        if self:
            preorder.append(self.data)
            if self.left:
                preorder += self.left.preorder()
            if self.right:
                preorder += self.right.preorder()
        return preorder

    def inorder(self) -> List[Any]:
        """
        Time - O(N)
        Space - O(N)
        """
        inorder = []
        if self:
            if self.left:
                inorder += self.left.inorder()
            inorder.append(self.data)
            if self.right:
                inorder += self.right.inorder()
        return inorder

    def postorder(self) -> List[Any]:
        """
        Time - O(N)
        Space - O(N)
        """
        postorder = []
        if self:
            if self.left:
                postorder += self.left.postorder()
            if self.right:
                postorder += self.right.postorder()
            postorder.append(self.data)
        return postorder

    def search(self, key: Any) -> bool:
        """
        Time - O(N)
        Space - O(1)
        """
        if self is None:
            return False

        if key == self.data:
            return True
        elif key < self.data:
            if self.left:
                return self.left.search(key)
        elif key > self.data:
            if self.right:
                return self.right.search(key)
        return False
