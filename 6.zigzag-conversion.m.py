# -*- coding: utf-8 -*-
# @lc app=leetcode.cn id=6 lang=python
#
# [6] Z 字形变换
#

# @lc code=start
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        #slen = len(s)
        #numCol = slen % numRows
        #M[numRows][numCol] = []

        if numRows == 1 or len(s) <= numRows: return s

        curRow = 0
        r = [""] * numRows
        goingDown = False
        # 不要纠结于对字符串的序号的控制 这个地方仅仅对行递增或递减的问题
        for i in s:
            r[curRow] += i
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1
        
        return "".join(r)

# @lc code=end


if __name__ == "__main__":
    print Solution().convert("LEETCODEISHIRING", 3)
    print Solution().convert("LEETCODEISHIRING", 4)
