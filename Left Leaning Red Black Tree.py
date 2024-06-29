'''
Left leaning red-black tree
https://github.com/Iamubab/Left-Leaning-Red-Black-Tree/tree/master
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.color = 1
    def Print_tree(self, result=None):
        if result == None:
            result = []
        if self.left != None:
            self.left.Print_tree(result)
        result.append(self.data)
        if self.right != None:
            self.right.Print_tree(result)
        return result
class LLRBT:
    def __init__(self):
        self.tree = None

# Insert
    def Insert(self, val):
        if self.tree == None:
            self.tree = Node(val)
            self.tree.color = 0
        else:
            self.tree = self.__insert(self.tree, val)
            self.tree.color = 0
    def __insert(self, node, val):
        if node == None:
            return Node(val)
        if self.__isRed(node.left) and self.__isRed(node.right):
            self.__changecolor(node)
        if val < node.data:
            node.left = self.__insert(node.left, val)
        elif val > node.data:
            node.right = self.__insert(node.right, val)
        if self.__isRed(node.right) and not self.__isRed(node.left):
            node = self.__rotateLeft(node)
        if self.__isRed(node.left) and self.__isRed(node.left.left):
            node = self.__rotateRight(node)
        return self.fixUp(node)
    def __isRed(self, node):
        if node == None:
            return 0  # Nil nodes are black
        else:
            return (node.color == 1)

# Delete
    def Delete(self, val):
        if self.tree == None:
            return
        else:
            self.tree = self.__delete(self.tree, val)
    def __delete(self, node, val):
        if node == None: return node
        if val < node.data:
            if node.left == None or (not self.__isRed(node.left) and not self.__isRed(node.left.left)):
                node = self.__moveRedLeft(node)
            node.left = self.__delete(node.left, val)
        else:
            if self.__isRed(node.left):
                node = self.__rotateRight(node)
            if val == node.data and node.right == None:
                return None
            if node.right == None or (not self.__isRed(node.right) and not self.__isRed(node.right.left)):
                node = self.__moveRedRight(node)
            if val == node.data:
                node.data = self.__min(node.right)
                node.right = self.__deleteMin(node.right)
            else:
                node.right = self.__delete(node.right, val)
        return self.fixUp(node)
    def __deleteMin(self, node):
        if node.left == None:
            return None
        if node.left == None or (not self.__isRed(node.left) and not self.__isRed(node.left.left)):
            node = self.__moveRedLeft(node)
        node.left = self.__deleteMin(node.left)
        return self.fixUp(node)
    def __min(self, node):
        while node.left != None: node = node.left
        if node == None:
            return None
        else:
            return node.data

#Search node
    def __Node_in_tree(self, node, val):
        if node == None:
            return None
        if node.data == val:
            return node
        if val < node.data:
            return self.__Node_in_tree(node.left, val)
        else:
            if val > node.data:
                return self.__Node_in_tree(node.right, val)
    def Search(self, val):
        node = self.__Node_in_tree(self.tree, val)
        if node != None:
            return True
        elif node == None:
            return False


# Fixups
    def __changecolor(self, node):
        node.color = 1 - node.color
        if node.left is not None:
            node.left.color = 1 - node.left.color
        if node.right is not None:
            node.right.color = 1 - node.right.color
    def __rotateRight(self, node):
        originalLeft = node.left
        node.left = originalLeft.right
        originalLeft.right = node
        originalLeft.color = node.color
        node.color = 1
        return originalLeft
    def __rotateLeft(self, node):
        originalRight = node.right
        node.right = originalRight.left
        originalRight.left = node
        originalRight.color = node.color
        node.color = 1
        return originalRight
    def __moveRedRight(self, node):
        self.__changecolor(node)
        if node.left and self.__isRed(node.left.left):
            node = self.__rotateRight(node)
            self.__changecolor(node)
        return node
    def __moveRedLeft(self, node):
        self.__changecolor(node)
        if node.right and self.__isRed(node.right.left):
            node.right = self.__rotateRight(node.right)
            node = self.__rotateLeft(node)
            self.__changecolor(node)
        return node
    def fixUp(self, node):
        if self.__isRed(node.right):
            node = self.__rotateLeft(node)
        if self.__isRed(node.left) and self.__isRed(node.left.left):
            node = self.__rotateRight(node)
        if self.__isRed(node.left) and self.__isRed(node.right):
            self.__changecolor(node)
        return node

#Tree Visualization
import matplotlib.pyplot as plt
from pylab import rcParams
def plot_node(node, rb=True, level=1, posx=0, posy=0):
    width = 2000.0 * (0.5 ** (level))
    if node.color == 0 or rb == False:
        plt.text(posx, posy, str(node.data), horizontalalignment='center', color='k', fontsize=15)
    else:
        if node.color == 1 or rb == True:
            plt.text(posx, posy, str(node.data), horizontalalignment='center', color='r', fontsize=15)
    if node.left is not None:
        px = [posx, posx - width]
        py = [posy - 1, posy - 15]
        if node.left.color == 0 or rb == False:
            plt.plot(px, py, 'k-')
        else:
            plt.plot(px, py, 'r-')
        plot_node(node.left, rb, level + 1, posx - width, posy - 20)

    if node.right is not None:
        plot_node(node.right, rb, level + 1, posx + width, posy - 20)
        px = [posx, posx + width]
        py = [posy - 1, posy - 15]
        if node.right.color == 0 or rb == False:
            plt.plot(px, py, 'k-')
        else:
            plt.plot(px, py, 'r-')

def plot_tree(node, figsize=(20, 10)):
    if node.color == 1:
        rb = False
    elif node.color == 0:
        rb = True
    rcParams['figure.figsize'] = figsize
    fig, ax = plt.subplots()
    ax.axis('off')
    plot_node(node, rb)
    plt.show()
