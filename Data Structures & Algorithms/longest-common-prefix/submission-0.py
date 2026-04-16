class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        if "" in strs:
            return "" 
        newlst=sorted(strs,key=len)
        maxsub=newlst[0]
        while len(maxsub)>0:
            flag=1
            for i in range(1,len(newlst)):
                if maxsub in newlst[i]:
                    continue
                else:
                    maxsub=maxsub[0:len(maxsub)-1]
                    flag=0
                    break
            if flag==1:
                return maxsub
        return ""






