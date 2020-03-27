# -*- coding: utf-8 -*-
# @lc app=leetcode.cn id=21 lang=python
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

# @lc code=end

if __name__ == "__main__":

    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None

    a1 = ListNode(1)
    p = a1
    for i in [2, 4]:
        cur = ListNode(i)
        p.next = cur
        p = p.next

    b1 = ListNode(1)
    p = b1
    for i in [3, 4]:
        cur = ListNode(i)
        p.next = cur
        p = p.next

    r = Solution().mergeTwoLists(a1, b1)
    while r:
        print r.val
        r = r.next

    print "### case2 ###"
    a1 = ListNode(-10)
    p = a1
    for i in [-9, -6, -4, 1, 9, 9]:
        cur = ListNode(i)
        p.next = cur
        p = p.next

    b1 = ListNode(-5)
    p = b1
    for i in [-3, 0, 7, 8, 8]:
        cur = ListNode(i)
        p.next = cur
        p = p.next

    r = Solution().mergeTwoLists(a1, b1)
    while r:
        print r.val
        r = r.next
