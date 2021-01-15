class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])

        print (grid)

        ufs = []
        for i in range(rows):
            ufs.append(list(range(i*cols, (i+1)*cols)))

        def __x(v):
            return v % rows

        def __y(v):
            return int(v / cols)

        def find(x, y):
            v = ufs[y][x]
            if v != y*cols+x:
                ufs[y][x] = find(__x(v), __y(v))
            return ufs[y][x]


        def union(x1, y1, x2, y2):
            if x1 == x2 and y1 == y2:
                return
            v1, v2 = find(x1, y1), ufs[y2][x2]
            ufs[__y(v1)][__x(v1)] = find(__x(v2), __y(v2))


        def compress():
            for y in range(rows):
                for x in range(cols):
                    find(x, y)

        for y in range(rows):
            for x in range(cols):
                if x-1 > 0:
                    if grid[y][x] == grid[y][x-1] and grid[y][x] == '1':
                        union(x-1, y, x, y)
        
        # for x in range(cols):
        #     for y in range(rows):
        #         if y-1 > 0:
        #             if grid[y][x] == grid[y-1][x] and grid[y][x] == '1':
        #                 union(x, y-1, x, y)
                
        compress()

        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == '0':
                    ufs[y][x] = -1

        print(ufs)


s = Solution()
s.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])
# s.numIslands([
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ])