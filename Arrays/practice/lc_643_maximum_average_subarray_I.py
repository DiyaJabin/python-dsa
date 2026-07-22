#Time complexity: O(n)
#Space complexity: O(1)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left=0
        right=k-1
        window_sum=nums[0]
        for i in range(1,k):
            window_sum+=nums[i]
        max_sum=window_sum
        while right<len(nums)-1:
            right+=1
            window_sum=window_sum-nums[left]+nums[right]
            left+=1
            if window_sum>max_sum:
                max_sum=window_sum
        return max_sum/k
