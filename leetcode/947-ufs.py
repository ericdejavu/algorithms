class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        if not stones:
            return 0

        max_x, max_y = max([p[1] for p in stones]), max([p[0] for p in stones])

        _stones = []
        # build the map, X stone O no stone
        for y in range(max_y+1):
            _rows = []
            for x in range(max_x+1):
                if [x,y] in stones:
                    _rows.append('X')
                else:
                    _rows.append('O')
            _stones.append(_rows)
        print (_stones)

        rows, cols = len(_stones), len(_stones[0])

        ufs = []
        for i in range(len(_stones)):
            ufs.append(list(range(i*cols, (i+1)*cols)))
        
        def find(x, y):
            if ufs[y][x] == -1:
                return -1
            # print (x, y, ufs[y][x] % rows, int(ufs[y][x] / cols), ufs[y][x], cols*y+x)
            if ufs[y][x] != cols*y+x:
                ufs[y][x] = find(ufs[y][x] % rows, int(ufs[y][x] / cols))
            return ufs[y][x]

        def union(x1, y1, x2, y2):
            if x1 == x2 and y1 == y2 or (ufs[y1][x1] == -1 or ufs[y2][x2] == -1):
                return
            v = find(x1, y1)
            ufs[int(v / cols)][v % rows] = find(ufs[y2][x2] % rows, int(ufs[y2][x2] / cols))

        for y in range(rows):
            for x in range(cols):
                if _stones[y][x] == 'O':
                    ufs[y][x] = -1
            s_in_cols = cols
            for x in range(cols):
                if _stones[y][x] == 'X':
                    s_in_cols = x
                    break
            for z in range(s_in_cols, cols):
                if _stones[y][z] == 'X':
                    union(s_in_cols, y, z, y)

        for x in range(cols):
            s_in_rows = rows
            for y in range(rows):
                if _stones[y][x] == 'X':
                    s_in_rows = y
                    break
            if s_in_rows == rows:
                continue
            for z in range(s_in_rows, rows):
                if _stones[z][x] == 'X':
                    union(x, s_in_rows, x, z)

        # zip
        for x in range(cols):
            for y in range(rows):
                find(x, y)

        print (ufs)
        tmp = []
        for r in ufs:
            for i in r:
                tmp.append(i)
        
        l = len(set(tmp))-1
        if l == 0 and _stones[0][0] == 'X':
            l = 1

        ret = len(stones) - l

        print (ret)
        return ret
        


s = Solution()
s.removeStones([[0,1],[1,0],[1,1]])
s.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])
s.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]])
s.removeStones([[0,0],[0,1],[0,2],[1,0],[1,1],[2,0],[1,2],[2,1],[2,2]])
# s.removeStones([[3,3],[4,4],[1,4],[1,5],[2,3],[4,3],[2,4]])