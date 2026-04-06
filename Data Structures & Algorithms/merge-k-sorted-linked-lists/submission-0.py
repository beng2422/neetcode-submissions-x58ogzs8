# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        currLists = []
        for list1 in lists:
            currLists.append(list1.val)
            list1 = list1.next
        
        while lists:
            minVal = 10000
            index = 0
            for i in range(len(lists)):
                if minVal > lists[i].val:
                    minVal = lists[i].val
                    index = i

            res.append(minVal)
            lists[index] = lists[index].next
            if lists[index] == None:
                lists = lists[:index] + lists[index+1:]
        if len(res) == 0:
            return None
        pointer = ListNode(res[0])
        newVal = pointer
        for i in range(1, len(res)):
            node = ListNode(res[i])
            newVal.next = node
            newVal = newVal.next
            

        return pointer
        