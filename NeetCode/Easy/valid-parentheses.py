class Solution:
    def isValid(self, s):
        stack = []
        parentheses = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for c in s:
            if c in parentheses: # Açılış paranteziyse
                stack.append(c)
            else: # Kapanış paranteziyse
                if (len(stack) == 0):
                    return False

                top = stack.pop()

                if (parentheses[top] != c):
                    return False
        
        if (len(stack) != 0):
            return False
        else:
            return True
