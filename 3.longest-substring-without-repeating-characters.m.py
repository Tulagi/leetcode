# -*- coding: utf-8 -*-
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        his = {}
        maxlen = 0
        start = 0

        for i, j in enumerate(s):
            curlen = i - start + 1
            # 1.start不能往回跳
            # 2.start跳到本次重复字符的索引的下一位
            if j in his and start < his[j] + 1:
                    start = his[j] + 1
            else:
                maxlen = curlen if curlen > maxlen else maxlen
            his[j] = i

        return maxlen

# @lc code=end

if __name__ == "__main__":
    print Solution().lengthOfLongestSubstring("pwwkew")
    print Solution().lengthOfLongestSubstring("abcabcbb")
    print Solution().lengthOfLongestSubstring("bbbbbbbbbbb")
    print Solution().lengthOfLongestSubstring("dvdf")
    print Solution().lengthOfLongestSubstring("nfpdmpi")
    print Solution().lengthOfLongestSubstring("tmmzuxt")