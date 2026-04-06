# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if list1 and list2 and list1.val>list2.val:
        #     head = list2
        #     ret = list2
        # elif list1:
        #     head = list1
        #     ret = list1
        # elif list2:
        #     head = list2
        #     ret = list2
        # else:
        #     return list1
        head = ListNode()
        oldHead = head

        while list1 and list2:
          #  print(list1)
           # print(list2)
            if list1 and list2 and list1.val>list2.val:
                head.next = list2
                list2 = list2.next
            else:
                head.next = list1
                list1 = list1.next

            head = head.next


        if list1:
            head.next = list1
        if list2:
            head.next=list2
        return oldHead.next

        