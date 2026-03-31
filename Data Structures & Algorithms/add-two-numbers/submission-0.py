# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryover = 0
        newList = ListNode()
        temp = newList
        while l1 != None and l2 != None:
            working = l1.val + l2.val + carryover
            carryover = working // 10
            temp.next = ListNode(val=working % 10)
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        unadded = None
        if l1 == None and l2 == None:
            if carryover == 0:
                return newList.next
            else:
                temp.next = ListNode(val=carryover)
                return newList.next
        else:
            unadded = None
            if l1 == None:
                unadded = l2
            else:
                unadded = l1
            temp.next = unadded
            temp = temp.next
            while carryover != 0:
                print(f"carry: {carryover}, val: {temp.val}")
                working = temp.val + carryover
                carryover = working // 10
                temp.val = working % 10
                if temp.next == None:
                    break
                else:
                    temp = temp.next
            if carryover != 0:
                temp.next = ListNode(val=carryover)
            return newList.next