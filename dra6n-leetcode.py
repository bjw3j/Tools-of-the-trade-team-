'''
Daniel Arnette
February 24th, 2021
Tools of the Trade (CSC 3950/CS 1501)
Palindrome Test

Dont understand how to use GitHub
'''

#This is mostly modified from C++ code I did as a freshman

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False

        reversedPalin = 0
        originalPalin = x
        
        while x > 0:
            reversePalin = reversePalin * 10 + x % 10
            x = x // 10
            
        return reversePalin == originalPalin
