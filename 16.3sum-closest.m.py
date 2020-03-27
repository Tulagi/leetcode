# -*- coding: utf-8 -*-
# @lc app=leetcode.cn id=16 lang=python
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in xrange(n - 2):
            l = i + 1; r = n - 1
            while l < r:
                cur = nums[i] + nums[l] + nums[r]
                if abs(res - target) > abs(cur - target):
                    res = cur
                if cur > target: 
                    r -= 1
                elif cur < target:
                    l += 1
                else:
                    return res

        return res
# @lc code=end

if __name__ == "__main__":
    print Solution().threeSumClosest([-1, 2, 1, -4], 1)
    print Solution().threeSumClosest([0, 2, 1, -3], 1)
    print Solution().threeSumClosest([-1, 2, 1, -4], 1)
