class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic=dict()
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        result = []
        for num in dic:
            if dic[num] > len(nums) // 3:
                result.append(num)
        return result
        