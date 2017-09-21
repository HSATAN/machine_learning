# _*_ coding:utf-8 _*_


class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):

        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):

        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def get_insert(self, data):

        if self.leftChild is None and self.rightChild is None:
            return self
        if self.leftChild is None:
            if data <= self.key:
                return self
            else:

                self.get_insert(self.rightChild, data)
        else:
            if data >= self.key:
                return self
            else:
                return self.get_insert(self.leftChild, data)

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def insert(self, data):
        if self.leftChild is None and self.rightChild is None:
            if data <= self.key:
                node = BinaryTree(data)
                self.rightChild = node
                node.key = data


r = BinaryTree('a')
print r
print dir(r)
print r.key
data = 'b'
node = r.get_insert(data)

print node is r
print node

