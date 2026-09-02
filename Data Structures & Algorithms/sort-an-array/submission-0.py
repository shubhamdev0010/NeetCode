class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Base Case
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        # Step 1: Divide
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        # Step 2: Merge
        return self.Merge(left, right)

    def Merge(self, left: List[int], right: List[int]) -> List[int]:
        result = []
        i = 0
        j = 0
        
        # Compare Both array
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1
        
        while j < len(right):
            result.append(right[j])
            j += 1

        return result