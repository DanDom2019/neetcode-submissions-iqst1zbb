class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        clength=len(matrix[0])
        rlength=len(matrix)
        lowr=0
        highr=rlength-1
        lowc=0
        highc=clength-1
        found=False
        while lowr <=highr:
            midr=(lowr+highr)//2
            if matrix[midr][-1]>= target and matrix[midr][0] <= target:
                found=True
                break
            elif matrix[midr][-1] < target:
                lowr=midr+1
            else:
                highr = midr-1
        if found:
            while lowc <= highc:
                        midc= (lowc+highc)//2
                        if matrix[midr][midc]== target:
                            return True
                        elif matrix[midr][midc] < target:
                            lowc=midc+1
                        else:
                            highc=midc-1
        return False
        