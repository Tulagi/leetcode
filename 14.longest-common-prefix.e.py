# -*- coding: utf-8 -*-
# @lc app=leetcode.cn id=14 lang=python
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""

        n = 0
        minlen = min([len(s) for s in strs])
        for i in xrange(minlen):
            if len(set([s[i] for s in strs])) != 1:
                break
            n += 1
        return strs[0][:n]

#        if len(strs) == 0:
#            return ""
#        prefix = strs[0]  # 从第1个字符串开始
#        for i in range(len(strs)):
#            while(strs[i].find(prefix) != 0):  # 不是其他字符串的前缀
#                prefix = prefix[0: len(prefix)-1]  # 减少前缀
#                if not prefix:
#                    return ""
#        return prefix
        
# @lc code=end

if __name__ == "__main__":
    print Solution().longestCommonPrefix(["flower","flow","flight"])
    print Solution().longestCommonPrefix(["dog","racecar","car"])
    print Solution().longestCommonPrefix(["flower","flow","","flight"])
    print Solution().longestCommonPrefix(["aca","cba"])
