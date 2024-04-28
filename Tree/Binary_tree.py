from typing import Any
from typing import List


class BinaryTree:
    def __init__(self, data) -> None:
        """
        Time - O(1)
        Space - O(1)
        """
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert_left(self, data: Any):
        """
        Time - O(1)
        Space - O(1)
        """
        if self.left_child is None:
            self.left_child = BinaryTree(data)
            return self.left_child
        else:
            raise ValueError("Left child already exists.")

    def insert_right(self, data: Any) -> None:
        """
        Time - O(1)
        Space - O(1)
        """
        if self.right_child is None:
            self.right_child = BinaryTree(data)
            return self.right_child
        else:
            raise ValueError("Right child already exists.")

    def get_right(self) -> None:
        """
        Time - O(N)
        Space - O(N)
        """
        return self.right_child

    def get_left(self) -> None:
        """
        Time - O(1)
        Space - O(1)
        """
        return self.left_child

    def set_root(self, obj) -> None:
        """
        Time - O(1)
        Space - O(1)
        """
        self.data = obj

    def get_root(self) -> Any:
        """
        Time - O(1)
        Space - O(1)
        """
        return self.data

    def preorder(self) -> List[Any]:
        """
        Time - O(N)
        Space - O(N)
        """
        preorder = []
        if self:
            preorder.append(self.get_root())
            if self.get_left():
                preorder += self.get_left().preorder()
            if self.get_right():
                preorder += self.get_right().preorder()
        return preorder

    def inorder(self) -> List[Any]:
        """
        Time - O(N)
        Space - O(N)
        """
        inorder = []
        if self:
            if self.get_left():
                inorder += self.get_left().inorder()
            inorder.append(self.get_root())
            if self.get_right():
                inorder += self.get_right().inorder()
        return inorder

    def postorder(self) -> List[Any]:
        """
        Time - O(N)
        Space - O(N)
        """
        postorder = []
        if self:
            if self.get_left():
                postorder += self.get_left().postorder()
            if self.get_right():
                postorder += self.get_right().postorder()
            postorder.append(self.get_root())
        return postorder
