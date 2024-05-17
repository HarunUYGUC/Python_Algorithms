""" https://leetcode.com/problems/set-mismatch/ """

# Method 1 
# My code passed about 49 of 49 tests but was very slow. "Time Limit Exceeded"

class Solution:
    def findErrorNums(self, nums):
        list = [0, 0]

        for num in range(1, len(nums) + 1):
            if num in nums:
                count = nums.count(num)

                if (count == 2):
                    list[0] = num
            else:
                list[1] = num
        
        return list
    
print(Solution().findErrorNums([3,2,3,4,6,5]))


# Method 2 
# Again slow but much faster than the other one. I also beat 99.32% people in memory usage. "Accepted"
# 4315 ms and 17.7 MB

class Solution:
    def findErrorNums(self, nums):
        list = [0, 0]
        nums.sort()

        for num in range(1, len(nums) + 1):
            # If I write this code, it runs faster, but the memory usage increases slightly.
            # Beats 72.79% of users in memory usage. "Accepted"
            # 3383 ms and 18 MB

            # if (list[0] != 0) and (list[1] != 0):
            #     break

            if num not in nums:
                list[1] = num
            else:
                nums.remove(num)

                if (nums.count(num) == 1):
                    list[0] = num
                    
        return list

print(Solution().findErrorNums([3,2,3,4,6,5])) 
