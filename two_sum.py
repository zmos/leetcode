class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3_head = ListNode(0)
        l3 = l3_head
        tmp = 0
        while True:
            if l1 != None:
                tmp += l1.val
                l1 = l1.next
            if l2 != None:
                tmp += l2.val
                l2 = l2.next
            l3.val = tmp%10
            tmp = tmp/10
            if l1 == None and l2 == None:
                if tmp == 0:
                    return l3_head
                else:
                    l3.next = ListNode(tmp)
                    return l3_head
            else:
                l3.next = ListNode(tmp)  
                l3 = l3.next
