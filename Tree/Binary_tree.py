class BinaryTree:
    def __init__(self, data) -> None:
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert_left(self, data):
        if self.left_child is None:
            self.left_child = BinaryTree(data)
        else:
            t = BinaryTree(data)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, data):
        if self.right_child is None:
            self.right_child = BinaryTree(data)
        else:
            t = BinaryTree(data)
            t.right_child = self.right_child
            self.right_child = t

    def get_right(self):
        return self.right_child

    def get_left(self):
        return self.left_child

    def set_root(self, obj):
        self.data = obj

    def get_root(self):
        return self.data

    def preorder(self):
        if self:
            print(self.get_root())
            if self.get_left():
                self.get_left().preorder()
            if self.get_right():
                self.get_right().preorder()

    def inorder(self):
        if self:
            if self.get_left():
                self.get_left().inorder()
            print(self.get_root())
            if self.get_right():
                self.get_right().inorder()

    def postorder(self):
        if self:
            if self.get_left():
                self.get_left().postorder()
            if self.get_right():
                self.get_right().postorder()
            print(self.get_root())
