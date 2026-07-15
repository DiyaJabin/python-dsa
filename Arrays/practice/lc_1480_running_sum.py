#Approach 1- creating a new list
#Time complexity - O(n), space complexity = O(n)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum_list=[]
        current_sum=0
        for num in nums:
            current_sum+=num
            running_sum_list.append(current_sum)
        return running_sum_list
    

#Approach 2- modifying the input itself
#Time complexity - O(n), space complexity - O(1)
class Solution:
    def runningSum(self,nums: List[int]) ->List[int]:
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        return nums
