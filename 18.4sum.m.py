# -*- coding: utf-8 -*-
# @lc app=leetcode.cn id=18 lang=python
#
# [18] 四数之和
#

# @lc code=start
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        n = len(nums)
        if n < 4:
            return []
        
        res = []
        nums.sort()
        for i in xrange(n - 3):
            if i > 0 and nums[i] == nums[i - 1]: 
                continue
            if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            for j in xrange(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]: 
                    continue
                if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                l = j + 1
                r = n - 1
                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] > target:
                        while l < r and nums[r] == nums[r - 1]: 
                            r -= 1
                        r -= 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        r -= 1
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        l += 1
        return res


# @lc code=end

if __name__ == "__main__":
    print Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
    # [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    print Solution().fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0)
    print Solution().fourSum([0, 0, 0, 0], 0)
    # [[-4,0,1,2],[-1,-1,0,1]]
    print Solution().fourSum([-1, 0, 1, 2, -1, -4], -1)
