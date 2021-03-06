prices = [1,2,3,4,5]
def maxProfit(prices):
    n = len(prices)
    if n < 2: return 0
    p1, p2 = prices[0], prices[n-1]
    profit1, profit2 = [0]*n, [0]*(n+1)
    for i in range(1,n):
        profit1[i] = max(profit1[i-1],prices[i] - p1)
        p1 = min(p1, prices[i])
        j = n-1-i
        profit2[j] = max(profit2[j+1],p2 - prices[j])
        p2 = max(p2, prices[j])
    profit = 0
    print(profit1)
    print(profit2)
    for i in range(n):
        profit = max(profit, profit1[i] + profit2[i])
    return profit
print(maxProfit(prices))