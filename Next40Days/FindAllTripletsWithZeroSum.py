Today's Problem is -

Given an array arr[], find all possible triplets i, j, k in the arr[] whose sum of elements is equals to zero. 
Returned triplet should also be internally sorted i.e. i<j<k.

Examples:

Input: arr[] = [0, -1, 2, -3, 1]
Output: [[0, 1, 4], [2, 3, 4]]
Explanation: Triplets with sum 0 are:
arr[0] + arr[1] + arr[4] = 0 + (-1) + 1 = 0
arr[2] + arr[3] + arr[4] = 2 + (-3) + 1 = 0
Input: arr[] = [1, -2, 1, 0, 5]
Output: [[0, 1, 2]]
Explanation: Only triplet which satisfies the condition is arr[0] + arr[1] + arr[2] = 1 + (-2) + 1 = 0
Input: arr[] = [2, 3, 1, 0, 5]
Output: [[]]
Explanation: There is no triplet with sum 0.
Constraints:
3 <= arr.size() <= 103
-104 <= arr[i] <= 104

Solution
Code-

class Solution:
    def findTriplets(self, arr):
        n = len(arr)
        triplets = set()

        
        value_to_indices = {}
        for idx, val in enumerate(arr):
            if val not in value_to_indices:
                value_to_indices[val] = []
            value_to_indices[val].append(idx)

        
        for i in range(n - 1):
            for j in range(i + 1, n):
                complement = - (arr[i] + arr[j])
                if complement in value_to_indices:
                    for k in value_to_indices[complement]:
                        if k > j: 
                            triplets.add((i, j, k))

        
        return sorted([list(t) for t in triplets])
