class Tree:
	def __init__(self,v = None):
		self.left = None
		self.right = None
		self.val = v

	def set(self,l,r):
		self.left = l
		self.right = r

class TreeList:
    def __init__(self):
        self.tmp = []
        self.root = None

    def insert(self, node, v):
        if not node:
            self.root = Tree(v)
            return
        if v < node.val:
            if not node.left:
                node.left = Tree(v)
                return
            self.insert(node.left, v)
        else:
            if not node.right:
                node.right = Tree(v)
                return
            self.insert(node.right, v)

    def build(self):
        for i in range(10):
            self.insert(self.root, i)

    def order(self, node):
    	if node == None:
    		return
    	self.tmp.append(node.val)
    	self.order(node.left)
    	self.order(node.right)

    def run(self):
        self.build()
        self.order(self.root)
        print self.tmp

tree = TreeList()
tree.run()
