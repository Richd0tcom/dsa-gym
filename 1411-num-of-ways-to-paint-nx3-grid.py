"""
You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.

 

Example 1:


Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown.
Example 2:

Input: n = 5000
Output: 30228214
 

Constraints:

n == grid.length
1 <= n <= 5000
"""



class Solution:
    """
    Let the three colors be 0, 1, and 2. For a row with columns c1, c2, c3:
	•	c1 != c2 and c2 != c3 (Standard row constraint).
We can categorize all valid row states into two distinct patterns based on whether the first and last colors are the same:
	•	Type A (ABA Pattern): The first and last colors are the same (c1 == c3).
	◦	Example: Red-Yellow-Red, Green-Red-Green.
	◦	Since c1 must differ from c2, there are 3 x 2 x 1 = 6 such combinations for a single row.
	•	Type B (ABC Pattern): The first and last colors are different (c1 != c3).
	◦	Example: Red-Yellow-Green, Green-Red-Yellow.
	◦	Since all three adjacent pairs must be different, this implies all three colors in the row are distinct. There are 3 x 2 x 1 = 6 such combinations for a single row.
3. Transitions Between Rows
We define two variables for our dynamic programming approach:
	•	A_i: Number of ways to paint the first i rows such that the i-th row is Type A (ABA).
	•	B_i: Number of ways to paint the first i rows such that the i-th row is Type B (ABC).
We calculate A_{i+1} and B_{i+1} based on the values of the previous row A_i and B_i.
Transitions from a Type A (ABA) row:
If the previous row was ABA (e.g., 1-2-1):
	•	To a new Type A (ABA): There are 3 valid patterns.
	•	To a new Type B (ABC): There are 2 valid patterns.
Transitions from a Type B (ABC) row:
If the previous row was ABC (e.g., 1-2-3):
	•	To a new Type A (ABA): There are 2 valid patterns.
	•	To a new Type B (ABC): There are 2 valid patterns.

4. The Recurrence Relation
Combining these observations, we get the following formulas:
A_{i+1} = 3 x Ai+ 2 x Bi
B_{i+1} = 2x Ai+ 2 x Bi
Base Case (n=1):
	•	A1 = 6
	•	B1 = 6
Total Ways:
For a grid of size n, the answer is (A_n + B_n) mod{10^9 + 7}.
    """
    def numOfWays(self, n: int) -> int:
        mod = (10**9) +7

        #base case
        type_A = 6
        type_B = 6

        for i in range(2, n+1):

            new_type_A =  (3 * type_A) + (2 * type_B)
            new_type_B = (2 * type_A) + (2 * type_B)

            type_A = new_type_A
            type_B = new_type_B
        
        return (type_A + type_B) % mod