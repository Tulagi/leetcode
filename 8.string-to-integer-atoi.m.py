# -*- coding: utf-8 -*-
# @lc app=leetcode.cn id=8 lang=python
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        if not str:
            return 0
        if str[0] not in " -+0123456789":
            return 0

        INT_MAX = (1 << 31) - 1
        INT_MIN = - (1 << 31)        

        pos = True
        go = False
        start = 0
        end = 0
        for i, j in enumerate(str):
            if j == ' ' and not go:
                start = end = i + 1
            elif j in '-+' and not go:
                pos = False if j == '-' else True
                start = end = i + 1
                go = True
            elif j in "0123456789":
                end += 1
                go = True
            else:
                break
        
        if start == end:
            return 0
        int_ret = int(str[start:end])
        int_ret = int_ret if pos else -int_ret
        if int_ret > INT_MAX:
            return INT_MAX
        if int_ret < INT_MIN:
            return INT_MIN
        return int_ret

# @lc code=end

if __name__ == "__main__":
    print Solution().myAtoi("42")
    print Solution().myAtoi("   -42")
    print Solution().myAtoi("words and 987")
    print Solution().myAtoi("4193 with words")
    print Solution().myAtoi("-91283472332")
    print Solution().myAtoi("99999999999991283472332")
    print Solution().myAtoi("  0000000000012345678")
