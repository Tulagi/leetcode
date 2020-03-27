# -*- coding: utf-8 -*-
# @lc app=leetcode.cn id=13 lang=python
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman2nums = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, 
                      "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}

        num = 0
        # 遍历对象是s 而不是roman序列 一定注意
        while s:
            r = s[0: 2]
            if r in roman2nums:
                num += roman2nums[r]
                s = s[2:]
            else:
                num += roman2nums[s[0]]
                s = s[1:]
        return num


# @lc code=end

if __name__ == "__main__":
    print Solution().romanToInt("III")
    print Solution().romanToInt("IV")
    print Solution().romanToInt("IX")
    print Solution().romanToInt("LVIII")
    print Solution().romanToInt("MCMXCIV")
