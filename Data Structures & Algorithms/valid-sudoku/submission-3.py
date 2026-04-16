from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''Best Implementation of the solution.
        Here we take 3 hashmaps each corresponding to row,column 
        and subbox check for validity...
        For each hashmap,  
        key->index of row/column/subbox  , Val-> Set to store the elems'''
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)  # Key: (r//3, c//3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val == ".":
                    continue
                
                # Check if value already exists in current row, column, or 3x3 square
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in squares[(r // 3, c // 3)]):
                    return False
                
                # Add value to the sets
                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3, c // 3)].add(val)
                
        return True