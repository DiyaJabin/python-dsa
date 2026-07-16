#Time complexity: O(n)
#Space complexity: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        reader=1 #scans every element exactly once
        writer=0 #keeps track of the last unique element 
        while reader<len(nums): #writer can never overtake the reader
            if nums[reader]!=nums[writer]:
                writer+=1
                nums[writer]=nums[reader]
            reader+=1 

        return writer+1

