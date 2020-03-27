# -*- coding: utf-8 -*-
# @lc app=leetcode.cn id=19 lang=python
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        p = head
        count = 1
        while p.next:
            count += 1
            p = p.next
        if count == n:
            return head.next

        x = count - n
        p = head
        q = head
        for _ in xrange(x):
            q = p
            p = p.next
        q.next = p.next

        return head

# @lc code=end

if __name__ == "__main__":

    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None
    
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a4 = ListNode(4)
    a5 = ListNode(5)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5

    print "### a ###"
    r = Solution().removeNthFromEnd(a1, 2)
    while r:
        print r.val
        r = r.next

    print "### b ###"
    b1 = ListNode(1)
    r = Solution().removeNthFromEnd(b1, 1)
    while r:
        print r.val
        r = r.next

    print "### c ###"
    c1 = ListNode(1)
    c2 = ListNode(2)
    c1.next = c2
    r = Solution().removeNthFromEnd(c1, 2)
    while r:
        print r.val
        r = r.next
