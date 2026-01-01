from collections import deque
from typing import List

class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        new_arr = deque([])

        if (digits[-1] + 1) > 9:
            carry = 1
            new_arr.appendleft(0)
        else:
            new_arr.appendleft(digits[-1]+1)


        for i in range(len(digits)-2, -1, -1):

            print("d: ",digits[i])
            print("carry: ", carry)
            if (digits[i] + carry) > 9:
                carry = 1
                new_arr.appendleft(0)
            else:
                new_arr.appendleft(digits[i] + carry)
                carry = 0

        if carry == 1:
            new_arr.appendleft(carry)

        return list(new_arr)


s = Solution()
print(s.plusOne([8,9,9,9]))

           



