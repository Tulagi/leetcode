# -*- coding: utf-8 -*-
# @lc app=leetcode.cn id=27 lang=python
#
# [27] 移除元素
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        dup = []
        for i, j in enumerate(nums):
            if val == j:
                dup.append(i)
        for i in dup[::-1]:
            nums.pop(i)

        return len(nums)

# @lc code=end

if __name__ == "__main__":

    print "### case1 ###"
    nums = [3,2,2,3]
    r = Solution().removeElement(nums, 3)
    for i in xrange(r):
        print nums[i]

    print "### case2 ###"
    nums = [0,1,2,2,3,0,4,2]
    r = Solution().removeElement(nums, 2)
    for i in xrange(r):
        print nums[i]
