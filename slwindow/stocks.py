
from typing import List
class Solution:
    def bestStock(self, prices: List[int]) -> int:
        buy_day = 0
        sell_day = buy_day+1
        best = 0
        min_ = a[0]
        while sell_day<len(a):
            buy_price = a[buy_day]
            min_ = buy_price
            sell_price = a[sell_day]
            
            if sell_price<buy_price:
                if sell_price<min_:
                    buy_day=sell_day-1
                
                sell_day+=1
                buy_day+=1
            else:
                sell_day+=1
            diff = sell_price-buy_price
            if diff>best:
                best = diff


if __name__ == "__main__":
    new_ = Solution()
    a = [2,1,2,1,0,1,2]
    answer = new_.bestStock(a)
    print(answer)


