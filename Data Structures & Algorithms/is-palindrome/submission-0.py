class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = []
        reverse = []
        
        for letter in s:
            if letter.isalnum():
                letters.append(letter.lower())
                
        print(letters)
        for letter in reversed(s):
            if letter.isalnum():
                reverse.append(letter.lower())

        if letters == reverse:
            return True
        else:
            return False

        