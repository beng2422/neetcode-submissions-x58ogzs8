class MedianFinder:

    def __init__(self):
        self.median = None
        self.sorted_list = []
        

    def addNum(self, num: int) -> None:
        #Just use binary sort to insert
        left = 0
        right = len(self.sorted_list)-1
        # if right == -1:
        #     self.sorted_list.append(num)
        #     return

        while left<=right:
            
            mid = (left+right)//2
            # if self.sorted_list[mid]<=num and num<=self.sorted_list[mid+1]:
            #     self.sorted_list = self.sorted_list[:mid]+[num]+self.sorted_list[mid+1:]
            #     break
            if self.sorted_list[mid]>num:
                right=mid-1
            else:
                left=mid+1
        self.sorted_list.insert(left, num)



        

    def findMedian(self) -> float:
        if len(self.sorted_list)%2==0:
            return (self.sorted_list[len(self.sorted_list)//2-1] + self.sorted_list[len(self.sorted_list)//2] )/2.0
        else:
            return float(self.sorted_list[len(self.sorted_list)//2])
        

        
        