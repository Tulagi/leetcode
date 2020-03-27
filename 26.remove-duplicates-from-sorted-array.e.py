# -*- coding: utf-8 -*-
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # case 1
        n = len(nums)
        if n == 0:
            return 0
        dup = []
        for i in xrange(n):
            if i > 0 and nums[i] == nums[i - 1]:
                dup.append(i)
        for i in dup[::-1]:
            nums.pop(i)
        return len(nums)

        # case 2
        '''
        n = len(nums)
        if n == 0:
            return 0
        new_nums = nums[::-1]
        for i, j in enumerate(new_nums):
            if i > 0 and new_nums[i] == new_nums[i - 1]:
                nums.pop(n - i - 1)
        return len(nums)
        '''

        # case 3
        '''
        #  i:慢指针, j:快指针
        n = len(nums)
        if n == 0:
            return 0
        i = 0
        for j in xrange(1, n):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
        '''


# @lc code=end

if __name__ == "__main__":
    print Solution().removeDuplicates([1,1,2])
    print Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])
