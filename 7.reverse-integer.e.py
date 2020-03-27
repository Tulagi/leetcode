# -*- coding: utf-8 -*-
# @lc app=leetcode.cn id=7 lang=python
#
# [7] 整数反转
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 2147483647
        MAX = ((1 << 31) - 1) / 10

        res = 0
        b = False
        if x < 0:
            b = True
            x = -x
        while x:
            # 判断MAX和res求值的顺序可不能反了
            if res > MAX:
                return 0
            res = res * 10 + x % 10
            x = x / 10

        return res if not b else -res

# @lc code=end

if __name__ == "__main__":
    print Solution().reverse(123)
    print Solution().reverse(-123)
    print Solution().reverse(120)
    print Solution().reverse(-2147483412)

    print Solution().reverse(2147483647)
    print Solution().reverse(-2147483648)
