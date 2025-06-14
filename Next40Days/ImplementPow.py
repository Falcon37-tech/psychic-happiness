Today's problem is -

Implement the function power(b, e), which calculates b raised to the power of e (i.e. b^e).

Examples:

Input: b = 3.00000, e = 5
Output: 243.00000
Input: b = 0.55000, e = 3
Output: 0.16638
Input: b = -0.67000, e = -7
Output: -16.49971
Constraints:

-100.0 < b < 100.0
-10^9 <= e <= 10^9
Either b is not zero or e > 0.
-10^4 <= be <= 10^4

Solution

Code-
#User function Template for python3
class Solution:
    def power(self, b: float, e: int) -> float:
        if e == 0:
            return 1.0
            
        negative_exponent = e < 0
        e = abs(e)
        result = 1.0
            
        while e > 0:
            if e % 2 == 1:
                result *= b
            b *= b
            e //= 2
                
        if negative_exponent:
            result = 1.0 / result
            
        return round(result, 5)
