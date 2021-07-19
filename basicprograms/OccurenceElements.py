class Solution:

    # count the occurences of an element in an array
    def countOccurrences(self, arr, n, x):

        res = 0
        for i in range(n):
            if x == arr[i]:
                res += 1
        return res

    # count the zeroes in the list/array
    def moveZeroes(self, arr):

        value = input('enter a number')
        for i in range(len(arr)):
            if arr[i] == value:
                arr.append(arr.pop(arr.index(value)))
        return arr

    # occurences of characters in a string
    def occurencesCharOfString(self, str, c):

        res = ''
        for i in range(len(str)):
            # this one if they have specific character to display
            if c == str[i]:
                # or we can just display all the characters/string
                res += str[i]
        # returns the total number of elements
        return (len(str), res)



# calling function

output = Solution()
result = output.moveZeroes([1,2,0,3,0,1])
print(result)

output = Solution()
result = output.countOccurrences([1,2,3,1,1], 5, 1 )
print(result)

output = Solution()
result = output.occurencesCharOfString('test', 't')
print(result)