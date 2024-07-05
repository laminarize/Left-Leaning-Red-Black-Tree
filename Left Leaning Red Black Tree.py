class Node:
    def __init__(self, data):
        self.data = [data, 1]
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
            if self.Search(val) == False:
                self.tree = self.__insert(self.tree, val)
                self.tree.color = 0
    def __insert(self, node, val):
        if node == None:
            return Node(val)
        if val < node.data[0]:
            node.data[1] += 1
            node.left = self.__insert(node.left, val)
        elif val > node.data[0]:
            node.data[1] += 1
            node.right = self.__insert(node.right, val)
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
        if val < node.data[0]:
            if node.left == None or (not self.__isRed(node.left) and not self.__isRed(node.left.left)):
                node = self.__moveRedLeft(node)
            node.left = self.__delete(node.left, val)
        else:
            if self.__isRed(node.left):
                node = self.__rotateRight(node)
            if val == node.data[0] and node.right == None:
                return None
            if node.right == None or (not self.__isRed(node.right) and not self.__isRed(node.right.left)):
                node = self.__moveRedRight(node)
            if val == node.data[0]:
                node.data[0] = self.__min(node.right)
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
            return node.data[0]

#Search node
    def __Node_in_tree(self, node, val):
        if node == None:
            return None
        if node.data[0] == val:
            return node
        if val < node.data[0]:
            return self.__Node_in_tree(node.left, val)
        else:
            if val > node.data[0]:
                return self.__Node_in_tree(node.right, val)
    def __min(self, node):
        while node.left != None: node = node.left
        if node == None:
            return None
        else:
            return node.data[0]
###################################################################################
    def __Lmedian(self, node, median_index, left_size=0):
        if node.left is not None:
            left_size = node.left.data[1]
        else:
            left_size = 0
        if left_size + 1 == median_index:
            return node
        if left_size < median_index:
            median_index -= (left_size + 1)
            node = self.__Lmedian(node.right, median_index)
        else:
            node = self.__Lmedian(node.left, median_index)
        return node
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
########$$$$$$$$$$$$$$$$$$$$$$$$$###############################
    def __find_successor(self, node):
        current = node.right
        while current.left is not None:
            current = current.left
        return current 
    def __median(self, node, case, median_index, left_size=0):
        if node.left is not None:
            left_size = node.left.data[1]
        else:
            left_size = 0
        if case == 'even':
            # Check for even case:
            if left_size == median_index - 1:  # Median is between this node and its successor
                successor = self.__find_successor(node)  # Find successor (smallest node in right subtree)
                return (node.data[0] + successor.data[0]) / 2  # Average of two values
            elif left_size < median_index - 1:
                median_index -= (left_size + 1)  # Adjust target for right subtree
                return self.__median(node.right, case, median_index)
            else:
                return self.__median(node.left, case, median_index)
        else:
            if left_size + 1 == median_index:
                return node
            if left_size < median_index:
                median_index -= (left_size + 1)
                node = self.__median(node.right, median_index)
            else:
                node = self.__median(node.left, median_index)
        return node
########$$$$$$$$$$$$$$$$$$$$$$$$$###############################
    def Search(self, val):
        node = self.__Node_in_tree(self.tree, val)
        if node != None:
            return True
        elif node == None:
            return False
    def find_min(self):
        """Finds and returns the node with the minimum value in the tree."""
        if self.tree is None:
            return None  # Tree is empty
        else:
            return self.__min(self.tree)
###################################################################################
    def Lmedian(self):
        """Finds and returns the node with the left median value in the tree."""
        root = self.tree
        if (root.left and root.right) is not None:
            if 0 <= root.right.data[1] - root.left.data[1] <= 1:
                return root.data[0]
        if root.left is not None:
            tree_size = root.data[1]
            median_index = tree_size // 2 + 1
            node = self.__Lmedian(root, median_index)
            return node.data[0]
        else:
            return root.data[0]
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    def median(self):
        """Finds and returns the node with the median value in the tree."""
        root = self.tree
        if (root.left and root.right) is not None:
            if root.right.data[1] - root.left.data[1] == 0:
                return root.data[0]
        if root.left is not None:
            tree_size = root.data[1]
            median_index = tree_size // 2
            if tree_size % 2 == 0:
                case = 'even'
                median_index = tree_size // 2
            else:
                case = 'odd'
                median_index = (tree_size + 1) // 2
            node = self.__median(root, case, median_index)
            return node
        else:
            return root.data[0]

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
####################################################################################################
            node.data[1], node.right.data[1] = node.data[1] - node.right.data[1], node.data[1]
            if node.right.left is not None:
                node.data[1] += node.right.left.data[1]
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            node = self.__rotateLeft(node)
        if self.__isRed(node.left) and self.__isRed(node.left.left):
####################################################################################################
            node.data[1], node.left.data[1] = node.data[1] - node.left.data[1], node.data[1]
            if node.left.right is not None:
                node.data[1] += node.left.right.data[1]
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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


nodes = list(range(1,9))
P06 = LLRBT()
for node in nodes:
    P06.Insert(node)
plot_tree(P06.tree,figsize=(20, 10))
print(f'Median: {P06.median()}')

# Time complexity of algorithm is O(log n) since traversing a red black balanced tree is worst case O(log n)
