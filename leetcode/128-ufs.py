class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dataset = list(set(nums))
        dataset.sort()
        headless = [ i for i in dataset[1:] ]
        org = {}
        for i,data in enumerate(dataset):
            org[data] = i
        link = list(range(len(dataset)))

        def find(idx):
            if link[idx] != idx:
                link[idx] = find(link[idx])
            return link[idx]

        def union(idx1, idx2):
            _idx1,_idx2 = org[idx1],org[idx2]
            link[find(_idx1)] = link[find(_idx2)]

        for i, data in enumerate(headless):
            if abs(data - dataset[i]) == 1:
                union(data, dataset[i])

        if len(dataset) > 2:
            if abs(dataset[len(dataset)-2] - dataset[len(dataset)-1]) == 1:
                union(dataset[len(dataset)-2], dataset[len(dataset)-1])

        pre = 0
        cnt = 0
        _max = 0
        for i in link:
            if i == pre:
                cnt += 1
            else:
                if cnt > _max:
                    _max = cnt
                cnt = 1
                pre = i
        if cnt > _max:
            _max = cnt
        return _max

s = Solution()
s.longestConsecutive([1, 0, -1])
s.longestConsecutive([100,4,200,1,3,2])
s.longestConsecutive([0,3,7,2,5,8,4,6,0,1])