class StockSpanner:

    def __init__(self):
        self.prices = []
        

    def next(self, price: int) -> int:
        #create a stack -> where stack[i] = (price, #of steps to a higher price)
        i = len(self.prices)-1
        #of steps
        steps = 1
        while i >= 0 and self.prices[i][0] <= price:
            val = self.prices.pop()
            steps += val[1]
            i -= 1
        self.prices.append((price, steps))
        return steps

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)