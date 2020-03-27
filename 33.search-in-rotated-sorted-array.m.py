# -*- coding: utf-8 -*-
# @lc app=leetcode.cn id=33 lang=python
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) / 2
            if target == nums[m]:
                return m
            if target > nums[0]:
                if nums[m] < target and nums[m] > nums[l]:
                    l = m
                elif nums[m] > target:
                    r = m
            el
        return

# @lc code=end

if __name__ == "__main__":
    print Solution().search([4,5,6,7,0,1,2], 0)
    print Solution().search([4,5,6,7,0,1,2], 3)
