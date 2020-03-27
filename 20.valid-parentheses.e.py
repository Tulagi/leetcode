# -*- coding: utf-8 -*-
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        match = {")": "(", "]": "[", "}": "{"}
        res = []
        for i in s:
            if i in match.values():
                res.append(i)
            elif not res or res[-1] != match[i]:
                return False
            else:
                res.pop()
        return True if not res else False

# @lc code=end

if __name__ == "__main__":
    print Solution().isValid("}")
    print Solution().isValid("){")
    print Solution().isValid("{}")
    print Solution().isValid("()[]{}")
    print Solution().isValid("(]")
    print Solution().isValid("([)]")
    print Solution().isValid("{[]}")
