""" https://leetcode.com/problems/defanging-an-ip-address/ """

class Solution:
    def defangIPaddr(self, address):
        address = address.replace(".", "[.]")
        return address
    
print(Solution().defangIPaddr("1.1.1.1"))
