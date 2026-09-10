class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dict = {}

        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        result = []
        for i in range(1, len(nums) + 1):
            if i not in dict:
                result.append(i)
        return result