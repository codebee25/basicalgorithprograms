class Solution:
    def sumMethod(self, num):
        # converting integer input to string
        value = str(num)
        # initializing sum
        sum = 0
        # iterating through the loop
        for i in range(len(value)):
            # adding the digits in the input. Example: 25(i/p) = 2+5 =7(o/p)
            sum += int(value[i])
        return sum

    def traverseArray(self, arr):
        # Traverse the array len(arr) is used only for array/string
        for i in range(len(arr)):
            # prints elements in an array in reverse order
           print(arr[len(arr)-i-1])

# caliing

output = Solution()
output.traverseArray([1,2,3,5,4])
# output = [4,5,3,2,1]

# calling function for twoSum

# output = Solution()
# result = output.sumMethod(25)
# print(result)
# result =  7
