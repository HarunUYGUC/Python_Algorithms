class Solution:
    def productExceptSelf(self, nums):
        zeros = nums.count(0)
        products = 1
        output = []
        
        if (zeros > 1):
            return [0] * len(nums)
        elif (zeros == 1):
            for num in nums:
                if (num != 0):
                    products *= num
                    output.append(0)
                else:
                    output.append("-")
            
            output[output.index("-")] = products
        else:
            for num in nums:
                products *= num

            for num in nums:
                output.append(int(products / num))
        
        return output
