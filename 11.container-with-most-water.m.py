# -*- coding: utf-8 -*-
# @lc app=leetcode.cn id=11 lang=python
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        are = 0
        l = 0
        r = len(height) - 1
        while True:
            lh = height[l]
            rh = height[r]
            cur = min(lh, rh) * (r - l)
            if cur > are:
                are = cur

            if lh < rh:
                l += 1
            else:
                r -= 1

            if l >= r:
                return are

# @lc code=end

if __name__ == "__main__":
    print Solution().maxArea([1,8,6,2,5,4,8,3,7])
