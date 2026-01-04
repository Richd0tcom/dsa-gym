import math



class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        """
“A number has exactly four divisors only if it is the product of two distinct primes or a cube of a prime. This allows us to skip divisor enumeration entirely.”
        """
        def is_prime(n: int) -> bool:
            if n < 2:
                return False
            for i in range(2, int(math.isqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True

        total = 0

        for num in nums:
            # Case 1: num = p^3
            p = round(num ** (1/3))
            if p ** 3 == num and is_prime(p):
                total += 1 + p + p * p + num
                continue

            # Case 2: num = p * q (p != q, both primes)
            for p in range(2, int(math.isqrt(num)) + 1):
                if num % p == 0:
                    q = num // p
                    if p != q and is_prime(p) and is_prime(q):
                        total += 1 + p + q + num
                    break

        return total
