class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstStringCount={}
        secondStringCount={}

        for cha in s:
            if cha not in firstStringCount:
                firstStringCount[cha]=0
            else:
                firstStringCount[cha]+=1
        for cha in t:
            if cha not in secondStringCount:
                secondStringCount[cha]=0
            else:
                secondStringCount[cha]+=1
        
        return firstStringCount == secondStringCount
            