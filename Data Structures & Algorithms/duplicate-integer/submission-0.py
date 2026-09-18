class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() 
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
sol = Solution()
result = sol.hasDuplicate([1,1,2,2,1])
print(result)
        