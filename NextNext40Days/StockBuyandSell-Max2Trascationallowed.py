Today's Problem is-

In daily share trading, a trader buys shares and sells them on the same day. If the trader is allowed to make at most 2 transactions in a day, find out the maximum profit that a share trader could have made.

You are given an array prices[] representing stock prices throughout the day. Note that the second transaction can only start after the first one is complete (buy->sell->buy->sell).

Examples:

Input: prices[] = [10, 22, 5, 75, 65, 80]
Output: 87
Explanation: 
Trader will buy at 10 and sells at 22. 
Profit earned in 1st transaction = 22 - 10 = 12. 
Then he buys at 5 and sell at 80. 
Profit earned in 2nd transaction = 80 - 5 = 75. 
Total profit earned = 12 + 75 = 87. 
Input: prices[] = [2, 30, 15, 10, 8, 25, 80]
Output: 100
Explanation: 
Trader will buy at 2 and sells at 30. 
Profit earned in 1st transaction = 30 - 2 = 28. 
Then he buys at 8 and sell at 80. 
Profit earned in 2nd transaction = 80 - 8 = 72. 
Total profit earned = 28 + 72 = 100.
Constraints:
1 <= prices.size() <= 10^5
1 <= prices[i] <= 10^5



Solution
Code-
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        left = [0]*n
        minprice = prices[0]
        for i in range(1, n):
            minprice = min(minprice, prices[i])
            left[i] = max(left[i-1], prices[i] - minprice)
            
        right = [0]*n
        maxprice = prices[-1]
        for i in range(n-2, -1, -1):
            maxprice = max(maxprice, prices[i])
            right[i] = max(right[i+1], maxprice - prices[i])
            
        maxprofit = 0
        for i in range(n):
            maxprofit = max(maxprofit, left[i]+right[i])
            
        return maxprofit
