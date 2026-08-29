class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_arr = list(set(nums))
        if len(new_arr) == len(nums):
            return False
        else:
            return True
            

    