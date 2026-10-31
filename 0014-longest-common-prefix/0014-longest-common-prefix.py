class Solution(object):
    def longestCommonPrefix(self, strs):
        """:type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Iterate through the indices of the first string
        for i in range(len(strs[0])):
            char = strs[0][i]
            # Check this character against all other strings
            for j in range(1, len(strs)):
                # If we reach the end of any string or a character doesn't match
                if i >= len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
                    
        return strs[0]