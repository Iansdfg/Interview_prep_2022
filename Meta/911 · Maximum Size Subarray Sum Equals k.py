class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def max_sub_array_len(self, nums, k):
        # Write your code here
        prefix_sum = 0
        ans = 0
        sum2ind = dict()
        for i in range(len(nums)):
            prefix_sum = prefix_sum + nums[i]

            if prefix_sum not in sum2ind:
                sum2ind[prefix_sum] = i
            if prefix_sum == k:
                ans = max(ans, i + 1)

            if prefix_sum - k in sum2ind:
                ans = max(ans, i - sum2ind[prefix_sum - k])

        return ans 
