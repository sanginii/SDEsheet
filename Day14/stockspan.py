class StockSpanner:

    def __init__(self):
        self.prices = []
        self.cur_ind = -1
    def next(self, price: int) -> int:
        self.cur_ind+=1
        while self.prices and price >= self.prices[-1][0]:
            self.prices.pop()
        ind = self.prices[-1][1] if self.prices else -1
        self.prices.append((price, self.cur_ind)) 
        days = self.cur_ind - ind
        return days 
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)