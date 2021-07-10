class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # looping through an array and storing the indices in i
        for i in range(len(nums)):
            # storing the indices from i+1 in j
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]

# call the function
output = Solution()
result = output.twoSum([1,2,3], 3)
print(result)
