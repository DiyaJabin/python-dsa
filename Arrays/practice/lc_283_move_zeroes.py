#Time complexity: O(n)
#Space complexity: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
       writer=0 #points to the first zero waiting to be replaced
       reader=1 #scans the array for non-zero elements
       while reader<len(nums):
        if nums[writer]!=0:
            writer+=1
        if nums[writer]==0 and nums[reader]!=0:
            nums[writer]=nums[reader]
            nums[reader]=0
            writer+=1
        reader+=1

        