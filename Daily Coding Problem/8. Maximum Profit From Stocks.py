'''You are given an array. Each element represents the price of a stock on that particular day. Calculate and return the
maximum profit you can make from buying and selling that stock only once.

For example: [9, 11, 8, 5, 7, 10]

Here, the optimal trade is to buy when the price is 5, and sell when it is 10, so the return value should be 5
(profit = 10 - 5 = 5).'''

def buy_and_sell(arr):
    lowest = arr[0]
    gain, maxgain = 0, 0    
    for val in arr[1:]:
        if val <= lowest:
            lowest = val
        else:
            gain = val - lowest
            if gain > maxgain:
                maxgain = gain           
    return maxgain

print (buy_and_sell([9, 11, 8, 5, 7, 10]))
# 5

# ---------------------------------------------------------------------------------------------------------------
# Another solution 

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