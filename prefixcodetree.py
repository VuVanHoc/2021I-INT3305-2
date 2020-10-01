import sys


class Node:
    def __int__(self, val):
        self.val = val

    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class PrefixCodeTree:
    def __init__(self):
        x1 = Node('x1', None, None)
        x2 = Node('x2', None, None)
        x3 = Node('x3', None, None)
        x4 = Node('x4', None, None)
        self.root = Node('root', x1, Node(None, Node(None, x2, x3), x4))

    @staticmethod
    def isLeaf(node):
        return node.left is None and node.right is None

    # add new node to tree
    def insert(self, codeword, symbol):
        # print(codeword, symbol)
        # for code in codeword:
        #     return
        pass

    def decode(self, encodedData, datalen):
        i = bin(int.from_bytes(encodedData, byteorder='big'))
        iStr = str(i)[2:datalen+2]
        print('Full String:', str(i))
        print('String bin :', iStr)
        result = ''
        node = self.root
        for i in iStr:
            if i == '0':
                node = node.left
            elif i == '1':
                node = node.right
            if self.isLeaf(node):
                result = result + node.val
                node = self.root

        print(result)
