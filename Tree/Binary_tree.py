class BinaryTree:
    def __init__(self, data) -> None:
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert_left(self, data):
        if self.left_child is None:
            self.left_child = BinaryTree(data)
        else:
            raise ValueError("Left child already exists.")

    def insert_right(self, data):
        if self.right_child is None:
            self.right_child = BinaryTree(data)
        else:
            raise ValueError("Rihgt child already exists.")

    def get_right(self):
        return self.right_child

    def get_left(self):
        return self.left_child

    def set_root(self, obj):
        self.data = obj

    def get_root(self):
        return self.data
