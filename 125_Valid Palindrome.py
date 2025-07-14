class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        S = ''.join(c.lower() for c in s if c.isalnum())

        n=len(S)
        if(n<=1):
            return True
        i=0
        while(i < n-i-1):
            if(S[i]!=S[n-i-1]):
                return False
            i=i+1
        return True
    

