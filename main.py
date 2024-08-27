from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        # Base case
        if n == 0:
            return [0]
        
        # Recursive case
        # Get the Gray code sequence for n-1 bits
        previous_gray_code = self.grayCode(n - 1)
        # Initialize the result list
        result = []
        
        # First half: prepend 0 to all previous_gray_code entries
        for code in previous_gray_code:
            result.append(code << 1)  # Equivalent to adding 0 at the end
        
        # Second half: prepend 1 to all previous_gray_code entries in reverse order
        for code in reversed(previous_gray_code):
            result.append((code << 1) | 1)  # Equivalent to adding 1 at the end
        
        return result

# Example usage:
sol = Solution()
print(sol.grayCode(2))  # Output: [0, 1, 3, 2]
print(sol.grayCode(1))  # Output: [0, 1]
