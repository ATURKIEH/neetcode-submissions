class Solution:
    def isPalindrome(self, s: str) -> bool:
        seen = []
        for letter in s:
            if letter.isalnum():
                seen.append(letter.lower())

        print(seen)
        print(seen[::-1])
        
        if seen == seen[::-1]:
            return True
        else:
            return False
        