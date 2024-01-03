class Solution:
    def findContentChildren(self, g, s):
        child = sorted(g)
        cookie = sorted(s)

        if len(child) == 0 or len(cookie) == 0:
            return 0
        
        if cookie[0] >= child[len(child)-1]:
            return min(len(cookie),len(child))
        else:
            mini = min(len(cookie),len(child))
            count = 0
            i = 0
            j = 0
            while i < len(child) and j < len(cookie) and count < mini:
                if child[i] <= cookie[j]:
                    count += 1
                    i += 1
                    j += 1
                else:
                    j += 1
            return count
solver = Solution()

g = [1,2,3]
s = [1,1]

print(solver.findContentChildren(g,s))