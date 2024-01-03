#https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/?envType=daily-question&envId=2024-01-03

class Solution:
    def numberOfBeams(self, bank) -> int:
        rows = len(bank)
        cols = len(bank[0])
        memo = {}
        for row in range(rows):
            memo[row] = -1 
        beams = 0
        row = 0
        #cycle for searching security devices
        while row < rows:
            if memo[row] == -1:
                count1 = 0
                count2 = 0
                #1. count how many devices there are on the row
                for col in range(cols):
                    if bank[row][col] == '1':
                        count1 += 1 
                if count1 > 0:
                #2. count how many devices there are on the next rows
                    j = row + 1
                    while j < rows and memo[j] == -1 and count2 == 0:
                        for i in range(cols):
                            if bank[j][i] == '1':
                                count2 += 1
                        memo[j] = count2
                        j += 1
                    if count2 > 0:
                        beams += count1 * count2
                    row += 1
                else:
                    row += 1
            else:
                count1 = memo[row]
                if count1 > 0 and row != rows - 1:
                    #check if there are devices on the next rows:
                    if memo[row+1] == -1:
                        count2 = 0
                        j = row + 1
                        while j < rows and memo[j] == -1 and count2 == 0:
                            for i in range(cols):
                                if bank[j][i] == '1':
                                    count2 += 1
                            memo[j] = count2
                            j += 1
                        if count2 > 0:
                            beams += count1 * count2
                        row += 1
                    else:
                        count2 = memo[row+1]
                        if count2 > 0:
                            beams += count1 * count2
                            row += 1
                else:
                    row += 1
        return beams
    
solver = Solution()
bank = ["000","111","000"]
print(solver.numberOfBeams(bank))