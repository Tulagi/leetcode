# -*- coding: utf-8 -*-
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ITEM_LEN = 2 * n
        res = []
        def do(item, left, right):
            if len(item) == ITEM_LEN:
                res.append(item)
                return
            
            if left < n:
                do(item + "(", left + 1, right)
            
            if right < left:
                do(item + ")", left, right + 1)
                
        do("", 0, 0)
        return res

# @lc code=end

if __name__ == "__main__":
    print Solution().generateParenthesis(1)
    print Solution().generateParenthesis(2)
    print Solution().generateParenthesis(3)
