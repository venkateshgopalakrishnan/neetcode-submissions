class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lookup = set(nums)
        return len(lookup) < len(nums)
