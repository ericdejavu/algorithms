def findRedundantConnection(edges):
    nodesCount = len(edges)
    parent = list(range(nodesCount + 1))

    def find(index):
        if parent[index] != index:
            parent[index] = find(parent[index])
        return parent[index]
    
    def union(index1, index2):
        if index1 == index2:
            return
        parent[find(index1)] = find(index2)

    for node1, node2 in edges:
        if find(node1) != find(node2):
            union(node1, node2)
        else:
            print (parent)
            print ([node1, node2])
            return [node1, node2]

    print (parent)
    return []


# findRedundantConnection([])
# findRedundantConnection([[1,2]])
# findRedundantConnection([[1,2], [1,3], [2,3]])
findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]])
findRedundantConnection([[1,3],[3,4],[1,5],[3,5],[2,3]])
findRedundantConnection([[1,2], [1,4], [2,3], [3,4], [3,5], [3,7], [5,6], [6,7]])