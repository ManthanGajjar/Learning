class Solution(object):
    def nextGreatestLetter(self, letters, target):
        for i in letters:
            if(target < i):
                return i
        return letters[0]