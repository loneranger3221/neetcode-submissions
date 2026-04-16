from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap=defaultdict(set)
        for i in range(9):
            set1=set()
            set2=set()
            #using empty set to check for seen elements and to terminate if already present
            for j in range(9):
                if board[i][j]=='.':
                    continue
                else:
                    if board[i][j] in set1 :
                        return False
                    else:
                        set1.add(board[i][j])

            for k in range(9):
                    if board[k][i]=='.':
                        continue
                    else:
                        if board[k][i] in set2:
                            return False
                        else:
                            set2.add(board[k][i])
                
                #subgrid index for 3 X 3 subboxes =(r/3,c/3)
                #in Hashmap for subbox check key->subgrid indx , val=check set
            for m in range(9):
                if board[i][m]=='.':
                    continue
                elif board[i][m] in hashmap[(i//3,m//3)]:
                    return False
                else:
                    hashmap[(i//3,m//3)].add(board[i][m])
            
        return True
        
            







            



