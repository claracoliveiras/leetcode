class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        word_one = sorted(list(s))
        word_two = sorted(list(t))
        if word_one == word_two:
            return True
        return False


        