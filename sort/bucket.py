def bucket(a):
	l = max(a)+1
	li = [0 for _ in range(l)]
	for i in a:
		li[i]+=1
	return [i for i,v in enumerate(li) for _ in range(0,v)]


if __name__ == '__main__':
	prex = [10,20,3,4,5,1,3,5,6,13,7,23,6]
	print bucket(prex)
