class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        prevMap = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
    
nums = [4,5,6]
target = 10
sol = Solution()
print(sol.twoSum(nums,target))