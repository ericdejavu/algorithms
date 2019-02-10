class Tree:
	def __init__(self,v):
		self.left = None
		self.right = None
		self.val = v
	def set(self,l,r):
		self.left = l
		self.right = r

datas = [x for x in range(20)]
nodes = [Tree(i) for i in datas]

# left x << 1
# right x << 1|1

def build():
	for p in range(1,len(datas)/2):
		_p = p<<1
		nodes[p].set(nodes[_p],nodes[_p+1])
	nodes[0] = nodes[1]

pre = []
mid = []
post = []

def preorder(node):
	if node == None:
		return
	pre.append(node.val)
	preorder(node.left)
	preorder(node.right)

def midorder(node):
	if node == None:
		return
	midorder(node.left)
	mid.append(node.val)
	midorder(node.right)

def postorder(node):
	if node == None:
		return
	postorder(node.left)
	postorder(node.right)
	post.append(node.val)
	print node.val

if __name__=='__main__':
	build()
	root = nodes[0]
	current = root
	preorder(root)
	midorder(root)
	postorder(root)
	print pre
	print mid
	print post
