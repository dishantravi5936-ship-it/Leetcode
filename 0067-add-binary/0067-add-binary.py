class Solution(object):
    def addBinary(self, a, b):
        result = []
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        
        while i >= 0 or j >= 0 or carry:
            sum_val = carry
            
            if i >= 0:
                sum_val += int(a[i])
                i -= 1
            if j >= 0:
                sum_val += int(b[j])
                j -= 1
                
            carry = sum_val // 2
            result.append(str(sum_val % 2))
            
        return "".join(result[::-1])