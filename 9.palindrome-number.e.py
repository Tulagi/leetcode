# -*- coding: utf-8 -*-
# @lc app=leetcode.cn id=9 lang=python
#
# [9] 回文数
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        strx = str(x)
        n = len(strx)

        if n == 1:
            return True

        l = 0; r = n - 1
        while True:
            if strx[l] != strx[r]:
                return False
            if l >= r:
                return True
            l += 1; r -= 1

# @lc code=end

if __name__ == "__main__":
    print Solution().isPalindrome(121)
    print Solution().isPalindrome(-121)
    print Solution().isPalindrome(10)
