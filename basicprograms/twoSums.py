class Solution:
    def twoSum(self, nums, target):
        # declaring the dictionary
        dict_list = {}
        # looping through for loop index
        for i in range(len(nums)):
            # storing the key, values as dict from list
            dict_list[i] = nums[i]
            # finding value
            value = target - dict_list[i]
            if value in dict_list.values():
                test = self.getKey(dict_list, value, i)
                if test != None:
                    return [test, i]

    # get the keys of dictionary
    def getKey(self, dict_list, input_value, index):
        for key, value in dict_list.items():
            if (input_value == value and index != key):
                return key;

            # call the function
output = Solution()
result = output.twoSum([1,2,3], 3)
print(result)
