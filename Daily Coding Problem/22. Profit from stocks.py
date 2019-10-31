# You are given an array. Each element represents the price of a stock on that particular day.
# Calculate and return the maximum profit you can make from buying and selling that stock only once.

def profit_from_stocks(prices):
    profit = 0
    maxprofit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i]-prices[i-1]
        else:
            profit = max(0, profit + prices[i] - prices[i-1])
        
        maxprofit = max(maxprofit, profit)
    return maxprofit
    
a = [9,11,8,5,7,16,17,18,1,2,3]
b = [1,2,3,4,2,3,4,5,6,7,3,4]
c = [10,11,12,1,2,3,4,6,7,0,7]

print(profit_from_stocks(c))
