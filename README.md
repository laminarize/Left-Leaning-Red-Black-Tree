## Left-Leaning-Red-Black-Tree
# Introduction:
A left leaning red black tree (LLRB) is a type of self balancing binary search tree in which each node is colored either red or black such that the root is black and the children of a red node are black. A red node is denoted by 1 whereas 0 for a black node. Every path from the root to a 0-node or a 1-node has the same number of black nodes. LLRB is a variant of Red Black Tree and guarantees the same asymptotic complexity for operations but is designed to be easier to implement.

# Properties:
Left-Leaning Red-Black tree exhibits six properties:
1. Red-Black tree must be a binary Search tree.
2. The root node must be colored BLACK
3. The children of Red colored node must be colored BLACK (no two consecutive RED nodes).
4. In all the paths of the tree, there should be same number of BLACK colored nodes.
5. Every new node must be inserted with RED color.
6. Every leaf (i.e. Null node) must be colored black.

# Implementation:
LLRB have been implemented in python programming language importing matplotlib library pyplot for visualisation. The major implementations are:
* Insert
* Delete
* Search
* Find True Median (LLRB.median)
* Find Left Median (LLRB.Lmedian)

After each insertion and deletion operation, a checkup is made in order to preserve RBT properties.
The algorithms have been extracted from (Introduction to Algorithms, Thomas H. Cormen) and (https://www.cs.princeton.edu/~rs/talks/LLRB/LLRB.pdf) to be implemented.

The basic test cases have been attached therewith, for the functionalities to be checked.
- Testcases_insert (INSERTION into the tree)
- Testcases_delete (DELETION from the tree)
- Testcases_search (To CHECK if node in tree)
