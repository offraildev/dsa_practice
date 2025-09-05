class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s # base case return same string

        result = ""

        # time complexity is < O(number_items_in_string), 
        # since numRows is a constant and second loop is better than O(number_items_in_string)
        # build solution row by row
        for r in range(numRows):
            increment = (numRows - 1) * 2
            for i in range(r, len(s), increment): # r goes from 0, 1, to numRows
                result += s[i]
                # in between the last and first row
                if r > 0 and r < numRows-1 and i + increment - r * 2 < len(s):
                    result += s[i + (increment - r * 2)]
        return result