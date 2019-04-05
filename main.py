from mytree import MyTree

#for heap
def heapsort (tree):
    """
    accepts tree
    """
    pass
t=MyTree()
with open ("words_39.txt",'r') as f:
    lines=f.readlines()
    for word in lines:
        print (word)
        t.insert(word)
