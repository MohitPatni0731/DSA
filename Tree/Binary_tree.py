class BinaryTree:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert_leftChild(self, data):
        if self.leftChild is None:
            self.leftChild = BinaryTree(data)
        else:
            print("Left child already exis.")

    def insert_rightChild(self, data):
        if self.rightChild is None:
            self.rightChild = BinaryTree(data)
        else:
            print("Right child already exist")

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.data = obj

    def getRootVal(self):
        return self.data
