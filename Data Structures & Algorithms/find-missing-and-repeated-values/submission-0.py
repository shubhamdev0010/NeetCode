class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        repeated = -1
        missing = -1
        count = {}

        for i in range(n):
            for j in range(n):
                val = grid[i][j]
                count[val] = count.get(val,0) + 1
                if count[val] == 2:
                    repeated = val

        for num in range(1, n*n + 1):
            if num not in count:
                missing = num
                break

        return [repeated, missing]