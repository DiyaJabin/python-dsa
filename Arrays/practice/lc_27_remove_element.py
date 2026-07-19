#Time complexity: O(n)
#Space complexity: O(1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        reader=0 #scans evefy element in the array
        writer=0 #points to the first ooccurence of 'val' that can be replaced 
        while reader<len(nums):
            if nums[writer]==val and nums[reader]!=val:
                nums[writer]=nums[reader]
                nums[reader]=val
                writer+=1
            if nums[writer]!=val: #if the current writer position already contains a valid element, move forward 
                writer+=1
            reader+=1
        return writer 
        