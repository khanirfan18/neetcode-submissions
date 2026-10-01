class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_one = sorted(list(s))
        list_two = sorted(list(t))

        if list_one == list_two:
            return True
        else:
            return False