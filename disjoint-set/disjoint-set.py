# graph disjoint_set
class GraphDisjointSet2D:
    def __init__(self, graph = None):
        if not graph:
            raise ValueError('graph cant be None')
        self.graph = graph
        self.rows, self.cols = len(graph), len(graph[0])
        self.ufs = []
        self.idxs = []
        for i in range(len(graph)):
            self.ufs.append(list(range(i*self.cols, (i+1)*self.cols)))
            for i in list(range(i*self.cols, (i+1)*self.cols)):
                self.idxs.append(i)

    def __x(self, v):
        return v % self.rows

    def __y(self, v):
        return int(v / self.cols)

    def find(self, x, y):
        v = self.ufs[y][x]
        if v != self.cols*y+x:
            self.ufs[y][x] = self.find(self.__x(v), self.__y(v))
        return self.ufs[y][x]

    def union(self, x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:
            return
        v1, v2 = self.find(x1, y1), self.ufs[y2][x2]
        self.ufs[self.__y(v1)][self.__x(v1)] = self.find(self.__x(v2), self.__y(v2))

    def is_connected(self, x1, y1, x2, y2):
        return self.ufs[y1][x1] == self.ufs[y2][x2]

    # after union completed
    def compress(self):
        for y in range(self.rows):
            for x in range(self.cols):
                if self.ufs[y][x] in self.idxs:
                    self.find(x, y)

    def print_ufs(self):
        print (self.ufs)

class AbstractDisjointSet:
    def __init__(self, links=None):
        if not links:
            raise ValueError('links cant be None')
        self.links = links
        self.ufs = []
        for i in range(len(l))

    def find(self, idx):
        if self.ufs[idx] != idx:
            self.ufs[idx] = self.find(self.ufs[idx])
        return self.ufs[idx]
    
    def union(self, idx1, idx2):
        self.ufs[self.find(idx1)] = self.find(idx2)