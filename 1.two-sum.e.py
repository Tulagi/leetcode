# -*- coding: utf-8 -*-
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        a = {}
        for i, j in enumerate(nums):
            b = target - j
            if b in a:
                return a[b], i
            a[j] = i

#print Solution().twoSum([2, 7, 11, 15], 9)
