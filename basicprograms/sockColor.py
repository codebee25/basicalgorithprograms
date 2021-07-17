from collections import Counter


class Solution:
    def sockColor(self, n, num):

        dictionary = {}
        for i in range(len(num)):
            dictionary[i] = num[i]
            count = Counter(dictionary.values())
            if count % 2 == 0:
                return False
            else:
                return {i, (count.value % 2)}

# calling function
output = Solution()
result = output.sockColor(6, [1,2,3,1,2,1])
