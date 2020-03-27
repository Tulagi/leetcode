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

        if not l1 and not l2:
            return None

        res = []
        if l1:
            p = l1
            while p:
                res.append({p.val: p, "val": p.val})
                p = p.next
        if l2:
            p = l2
            while p:
                res.append({p.val: p, "val": p.val})
                p = p.next

        res.sort()
        n = len(res)
        for i in xrange(n - 1):
            node1 = res[i][res[i]["val"]]
            node2 = res[i + 1][res[i + 1]["val"]]
            node1.next = node2
            #res[i].values()[0].next = res[i + 1].values()[0]
        #return res[0].values()[0]
        return res[0][res[0]["val"]]

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
