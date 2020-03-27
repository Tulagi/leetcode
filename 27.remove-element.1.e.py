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

        # 把不是去重的数移到前面去
        i = 0
        n = len(nums)
        for j in xrange(n):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

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
