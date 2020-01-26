nodes = [56, 33, 52, 91, 24, 12, 51, 41, 84, 19, 20, 31, 2, 3, 4, 5, 6, 7, 32, 1, 0, 65, 5, 6, 22, 13, 14, 21, 32, 41, 25, 64, 37, 89, 10, 47, 89, 34, 21, 9]
obtest = LLRBT()
for node in nodes:
    obtest.Insert(node)
plot_tree(obtest.tree,figsize=(20, 10))
obtest.Insert(20000)
plot_tree(obtest.tree,figsize=(20, 10))