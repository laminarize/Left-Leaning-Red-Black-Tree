obtest = LLRBT()
obtest.Delete(56)
obtest.Delete(7)
obtest.Delete(14)
obtest.Delete(1)
plot_tree(obtest.tree,figsize=(20, 10))