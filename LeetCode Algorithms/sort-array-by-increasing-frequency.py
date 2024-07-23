class Solution(object):
    def frequencySort(self, nums):
        numbers = []
        frequencies = []
        freq = 0

        # The numbers and frequency values ​​in the given list were found.
        while (len(nums) != 0):
            number = nums[0]
            numbers.append(number)
            
            for num in nums:
                if (num == number):
                    freq += 1
            
            frequencies.append(freq)

            while (freq != 0):
                nums.remove(number)
                freq -= 1
        
        # print(f"Numbers: {numbers}")
        # print(f"Frequencies: {frequencies}")

        result = []

        while (len(numbers) != 0):
            minFreq = min(frequencies)
            minFreqIndex = frequencies.index(minFreq)
            minNum = numbers[minFreqIndex]

            # If more than one value does not have the same frequency.
            piece = frequencies.count(minFreq)

            if (piece == 1):
                while (minFreq != 0):
                    result.append(minNum)
                    minFreq -= 1
                    
                numbers.pop(minFreqIndex)
                frequencies.pop(minFreqIndex)
            # If more than one value has the same frequency.
            else:
                list = []

                while (piece != 0):
                    minFreqIndex = frequencies.index(minFreq)
                    minNum = numbers[minFreqIndex]
                    
                    list.append(minNum)
                    piece -= 1

                    numbers.pop(minFreqIndex)
                    frequencies.pop(minFreqIndex)

                while (len(list) != 0):
                    maxNumList = max(list)
                    list.remove(maxNumList)
                    newMinFreq = minFreq
                    # print(maxNumList)

                    while (newMinFreq != 0):
                        result.append(maxNumList)
                        newMinFreq -= 1

                # print(list)

        # print(result)
        return result

# Solution().frequencySort([-1,1,-6,4,5,-6,1,4,1])
print(Solution().frequencySort([-1,1,-6,4,5,-6,1,4,1]))
