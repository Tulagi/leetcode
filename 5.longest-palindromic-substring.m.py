# -*- coding: utf-8 -*-
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        slen = len(s)
        longest = ""

        def getLongestPalindrome(c):
            # aba型
            l1 = r1 = c
            while l1 >= 0 and r1 < slen and s[l1] == s[r1]:
                l1 -= 1; r1 += 1
            # bb型
            l2 = c; r2 = c + 1
            while l2 >= 0 and r2 < slen and s[l2] == s[r2]:
                l2 -= 1; r2 += 1
            return s[l1 + 1: r1] if r1 - l1 > r2 - l2 else s[l2 + 1: r2]

        for i in xrange(slen):
            # 基于当前字符i 完成aba型和bb型的对称扩展 判断最长回文
            cur = getLongestPalindrome(i)
            if len(cur) > len(longest):
                longest = cur

        return longest

# @lc code=end

if __name__ == "__main__":
    print Solution().longestPalindrome("babad")
    print Solution().longestPalindrome("bbbbb")
