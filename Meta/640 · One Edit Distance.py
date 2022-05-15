class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def is_one_edit_distance(self, s, t):
        # write your code here
        len_s = len(s)
        len_t = len(t)

        if abs(len_s - len_t) > 1:
            return False

        #when len_s > len_t
        if len_s > len_t:
            return self.is_one_edit_distance(t, s)

        #when len_s < len_t
        for i in range(len_s):
            if s[i] != t[i]:
                if len_s == len_t:
                    return s[i+1:] == t[i+1:]
                return s[i:] == t[i+1:]


        return s != t





