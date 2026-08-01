class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        maxtillnow = -1  
        for i in range(n-1, -1, -1):
            newval = maxtillnow        
            if arr[i] > maxtillnow:
                maxtillnow = arr[i] 
            arr[i] = newval       
        return arr