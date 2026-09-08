class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        current_sum = nums[0]
        largest_sum = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                current_sum += nums[i]
            else:
                current_sum = nums[i]

            largest_sum  = max(largest_sum,current_sum)
        return largest_sum
        