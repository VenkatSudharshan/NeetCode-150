class Solution:
    def hasDuplicate(self, nums : list[int]) -> bool:
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
    

nums = [1,2,3,4]
nums2 = [1,2,3,1]
sol = Solution()
print(sol.hasDuplicate(nums))
print(sol.hasDuplicate(nums2))