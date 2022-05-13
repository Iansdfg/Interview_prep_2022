class Solution:
    """
    @param n: a integer
    @return: return a string
    """
    def convert_to_title(self, n):
        # write your code here
        res = self.rec(n)
        return res

        


    def rec(self, n):
        res = ''
        while n > 26:
            remiander = n % 26
            if remiander == 0:
                res = 'Z' + res 
                n = n//26 - 1
                continue
            res = chr(64 + remiander) + res 
            n = n//26

        res = chr(64 + n) + res
        return res 
             
