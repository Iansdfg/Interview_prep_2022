class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        index = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i] == nums[i-1]:
                nums.pop(i)
        return len(nums)
        


