# -*- coding: utf-8 -*-
# @lc app=leetcode.cn id=28 lang=python
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        return haystack.find(needle)

# @lc code=end

if __name__ == "__main__":
    print Solution().strStr("hello", "ll")
    # 空集是任何集合的子集
    print Solution().strStr("hello", "")
