# -*- coding: utf-8 -*-
# @lc app=leetcode.cn id=24 lang=python
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        first = True
        p = head
        q = head
        while p:
            x = p
            y = p.next
            if not y:
                break
            x.next = y.next
            y.next = x
            if first:
                head = y
            else:
                q.next = y
            first = False
            q = p
            p = p.next

        return head

# @lc code=end

if __name__ == "__main__":
    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None
    
    print "### case1 ###"
    case1 = [1, 2, 3, 4]
    c1 = ListNode(case1[0])
    p = c1
    for i in case1[1:]:
        p.next = ListNode(i)
        p = p.next

    r = Solution().swapPairs(c1)
    while r:
        print r.val
        r = r.next

    print "### case2 ###"
    case2 = [1, 2, 3, 4, 5]
    c2 = ListNode(case2[0])
    p = c2
    for i in case2[1:]:
        p.next = ListNode(i)
        p = p.next

    r = Solution().swapPairs(c2)
    while r:
        print r.val
        r = r.next
