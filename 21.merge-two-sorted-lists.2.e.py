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

class Solution:
    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        # 找个头 按序把l1和l2的节点缀上
        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # exactly one of l1 and l2 can be non-null at this point, so connect
        # the non-null list to the end of the merged list.
        # 遍历到最后把非空的列表全部缀上
        prev.next = l1 if l1 is not None else l2

        return prehead.next

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
