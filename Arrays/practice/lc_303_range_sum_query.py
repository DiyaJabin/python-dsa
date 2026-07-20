#Time complexity: __init__: O(n), sumRange: O(1)
#Space complexity: O(n)
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_array=[]
        current_sum=0 #Used only during preprocessing, so it doesn't need to be stored as an instance variable.
        for i in nums:
            current_sum+=i
            self.prefix_array.append(current_sum)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_array[right]-self.prefix_array[left-1] if left!=0 else self.prefix_array[right]
        