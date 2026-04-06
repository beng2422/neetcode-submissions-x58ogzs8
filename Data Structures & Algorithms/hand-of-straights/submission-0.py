class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:


        if len(hand) % groupSize != 0:
            return False
        newHand = [[] for i in range(len(hand)//groupSize)]
        for group in range(len(hand)//groupSize):
            print(newHand)
            print(hand)
            minVal = min(hand)
            hand.remove(minVal)

            for i in range(groupSize-1):
                 

                newHand[group].append(minVal)
                if minVal + 1 in hand:
                    minVal = minVal + 1
                    hand.remove(minVal)
                else:
                    return False

        return True
        