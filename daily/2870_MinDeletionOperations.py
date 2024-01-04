#https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/description/ 
class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_count = {}

        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1

        mini = 0

        # Procesar las ocurrencias
        for count in num_count.values():
            if count > 1:
                if count == 2 or count == 3:
                    mini += 1
                else:
                    k = count % 3
                    if k == 0:
                        n = (count-3)//3
                    else:
                        n = (count-k)//3
                    mini += n + 1
            else:
                return -1

        return mini
    
