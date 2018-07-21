# root node
pre_order = [1, 2, 4, 8, 16, 17, 9, 18, 19, 5, 10, 11, 3, 6, 12, 13, 7, 14, 15]
# root left and right nodes
mid_order = [16, 8, 17, 4, 18, 9, 19, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15]

def rebuild(pre,mid):
	if not mid or not pre:
		return
	root = Tree(pre[0])
	sp = mid.index(pre[0])
	root.left = rebuild(pre[1:sp+1],mid[:sp])
	root.right = rebuild(pre[sp+1:],mid[sp+1:])
	return root

root = rebuild(pre_order,mid_order)
