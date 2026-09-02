class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        result = []

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        for i in range(k):
            max_num = max(dic, key=dic.get)
            result.append(max_num)
            del dic[max_num]

        return result
