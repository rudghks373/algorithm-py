# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# ListNode{val: 2, next: ListNode{val: 4, next: ListNode{val: 3, next: None}}}
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        listl1 = self.changeList(l1)
        listl2 = self.changeList(l2)
        listl1.reverse()
        listl2.reverse()
        
        listl1Str = "".join(map(str,listl1))
        listl2Str = "".join(map(str,listl2))
        
        outputInt = int(listl1Str)+int(listl2Str)
        outputStr = str(outputInt)
        output = outputStr[::-1]
        node = None
        for i in range(len(output)-1,-1,-1):
            node = ListNode(output[i], node)
        return node

    def changeList(self, data):
        head = data
        tempList = []
        while 1:
            if head.val == 0 and head.next == None:
                tempList.append(0)
                break
            else:
                tempList.append(head.val)
                if head.next != None:
                    head = head.next
                else:
                    break
        return tempList
                    
