class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_list = [0]*36
        for ch,ch2 in zip(s,t):
            index1 = ord(ch) - 97
            index2 = ord(ch2) - 97
            hash_list[index1] +=1
            hash_list[index2] -=1

        for item in hash_list:
            if item != 0:
                return False
        
        return True
            

        

            