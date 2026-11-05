class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Traverse the array from the last digit to the first
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, it becomes 0, and the carry moves to the next digit
            digits[i] = 0
        
        # If all digits were 9 (e.g., [9, 9] -> [0, 0]), 
        # we need an extra digit at the beginning (e.g., [1, 0, 0])
        return [1] + digits