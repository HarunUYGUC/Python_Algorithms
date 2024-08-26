""" https://leetcode.com/problems/day-of-the-year/ """

# 8816 / 10958 testcases passed

class Solution:
    def dayOfYear(self, date):
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        totalDay = 0

        splited = date.split("-")
        monthIndex = int(splited[1]) - 1
        day = int(splited[2])
        
        for month in months[0:monthIndex]:
            totalDay += month

        totalDay += day
        return totalDay

print(Solution().dayOfYear("2003-03-01"))
