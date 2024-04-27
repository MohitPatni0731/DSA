class BinaryTree:
    def __init__(self, data) -> None:
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert_left(self, data):
        if self.left_child is None:
            self.left_child = BinaryTree(data)
            return self.left_child
        else:
            raise ValueError("Left child already exists.")

    def insert_right(self, data):
        if self.right_child is None:
            self.right_child = BinaryTree(data)
            return self.right_child
        else:
            raise ValueError("Right child already exists.")

    def get_right(self):
        return self.right_child

    def get_left(self):
        return self.left_child

    def set_root(self, obj):
        self.data = obj

    def get_root(self):
        return self.data

    def preorder(self):
        preorder = []
        if self:
            preorder.append(self.get_root())
            if self.get_left():
                preorder += self.get_left().preorder()
            if self.get_right():
                preorder += self.get_right().preorder()
        return preorder

    def inorder(self):
        inorder = []
        if self:
            if self.get_left():
                inorder += self.get_left().inorder()
            inorder.append(self.get_root())
            if self.get_right():
                inorder += self.get_right().inorder()
        return inorder

    def postorder(self):
        postorder = []
        if self:
            if self.get_left():
                postorder += self.get_left().postorder()
            if self.get_right():
                postorder += self.get_right().postorder()
            postorder.append(self.get_root())
        return postorder


r = BinaryTree(1)
r.insert_left(2)
r.insert_right(3)
r.get_left().insert_left(4)
print(r.preorder())
