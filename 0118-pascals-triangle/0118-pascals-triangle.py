class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []

        for row_idx in range(numRows):
            # Start a row of 1s with length equal to row_idx + 1
            row = [1] * (row_idx + 1)

            # Fill interior elements from index 1 to row_idx - 1
            for col_idx in range(1, row_idx):
                row[col_idx] = triangle[row_idx - 1][col_idx - 1] + triangle[row_idx - 1][col_idx]

            triangle.append(row)

        return triangle