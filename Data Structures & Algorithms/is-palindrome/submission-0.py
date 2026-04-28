class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we need to delete all non-alphanumeric characters
        # create two pointers 
        # while left pointer is less than or equal to the right pointer ->
        # move left pointer +1 and right pointer -1
        # at each step check whether the value of the string at both pointers is equal
        # if at any point the pointers don't match -> return False
        # once left pointer = right pointer -> return True

        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()

        return newStr == newStr[::-1]
    