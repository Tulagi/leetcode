# -*- coding: utf-8 -*-
# @lc app=leetcode.cn id=12 lang=python
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        if num in nums:
            return roman[nums.index(num)]
        
        res = ""
        for i in xrange(len(roman)):
            roman_char = roman[i]
            roman_num = nums[i]
            count = num / roman_num
            if count > 0:
                res += count * roman_char
                num -= count * roman_num

        return res

# @lc code=end

if __name__ == "__main__":
    print Solution().intToRoman(3)
    print Solution().intToRoman(4)
    print Solution().intToRoman(9)
    print Solution().intToRoman(41) # XLI
    print Solution().intToRoman(58)
    print Solution().intToRoman(1994)
    print Solution().intToRoman(3999)
