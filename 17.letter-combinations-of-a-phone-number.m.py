# -*- coding: utf-8 -*-
# @lc app=leetcode.cn id=17 lang=python
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        phone = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], 
                 "4": ["g", "h", "i"], "5": ["j", "k", "l"],
                 "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
                 "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

        n = len(digits)
        if n <= 1:
            return phone.get(digits, [])

        def combdig(item, dig):
            if not dig:
                res.append(item)
                return
            for i in phone[dig[0]]:
                combdig(item + i, dig[1:])

        res = []
        combdig("", digits)
        return res



# @lc code=end

if __name__ == "__main__":
    print Solution().letterCombinations("")
    print Solution().letterCombinations("2")
    print Solution().letterCombinations("23")
    print Solution().letterCombinations("234")
