# -*- coding: utf-8 -*-
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        p = l1
        q = l2
        res = None
        res_next = None
        carry = 0

        while (p or q):
            sum = (p.val if p else 0) + (q.val if q else 0) + carry
            if sum > 9:
                carry = 1
            else:
                carry = 0

            n = ListNode(sum % 10)
            if not res:
                res = n
                res_next = res
            else:
                res_next.next = n
                res_next = n

            p = p.next if p else None
            q = q.next if q else None
        
        if carry == 1:
            m = ListNode(1)
            n.next = m

        return res

# @lc code=end

if __name__ == '__main__':

    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None

    # l1
    l1 = ListNode(1)

    # l2
    l2 = ListNode(9)

    l2_1 = ListNode(9)
    l2.next = l2_1

    r = Solution().addTwoNumbers(l1, l2)
    while r:
        print "b: {}".format(r.val)
        r = r.next
