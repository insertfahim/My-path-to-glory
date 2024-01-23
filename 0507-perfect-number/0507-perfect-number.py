class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:  # Handle non-positive cases
            return False

        divisor_sum = 1  # Include 1 as a divisor
        i = 2
        while i * i <= num:  # Optimize by iterating up to the square root
            if num % i == 0:
                divisor_sum += i + num // i  # Add both divisors (if distinct)
            i += 1

        return divisor_sum == num
