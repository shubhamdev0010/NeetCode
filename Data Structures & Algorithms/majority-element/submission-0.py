class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = dict()

        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1

        n = len(nums)
        for key, value in dic.items():
            if value > n / 2:
                return key
                