#Time complexity=O(n)
#Space complexity=O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while numbers[left]+numbers[right]!=target:
            current_sum=numbers[left]+numbers[right]
            if current_sum<target:
                left+=1
            else:
                right-=1
        return [left+1,right+1]
    

#A more general approach would be to apply left<right for the while loop