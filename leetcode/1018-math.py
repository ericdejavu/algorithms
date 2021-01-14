class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        ret = []
        nums = 0
        for i, n in enumerate(A):
            nums *= 2
            nums += n
            ret.append(nums % 5 == 0)
        print (ret)
        return ret


s = Solution()
s.prefixesDivBy5([0,1,1])
s.prefixesDivBy5([1,1,1])
s.prefixesDivBy5([0,1,1,1,1,1])