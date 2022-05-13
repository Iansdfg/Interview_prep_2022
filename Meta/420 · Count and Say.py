class Solution:
    """
    @param n: the nth
    @return: the nth sequence
    """
    def count_and_say(self, n):
        # write your code here
        res = '1'
        if n == 1:
            return res 
        for i in range(n-1):
            res = self.countSay(res)
        return res


    def countSay(self, num):
        left = 0
        res = ''
        for right in range(len(num)):
            if num[right] != num[left]:
                cnt = right - left 
                say = num[left]
                res = res + str(cnt) + say
                left = right
        res = res + str(right - left + 1) + num[right]
        return res
            

