class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=1
        for j in range(len(nums)):
            if nums[j]!=nums[i]:
                nums[i+1]=nums[j]
                i=i+1 
        
    return i+1
