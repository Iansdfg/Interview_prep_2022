class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def is_match(self, s, p):
        # write your code here
        return self.is_match_helper(s, 0, p, 0, {})


    def is_match_helper(self, s, s_pointer, p, p_pointer, memo):
        if (s_pointer, p_pointer) in memo:
            return memo[(s_pointer, p_pointer)]
        # s empty
        if s_pointer >= len(s):
            return self.is_p_valid(p[p_pointer:])

        # p empty
        if p_pointer >= len(p):
            return False 

        # when * in p 
        if p_pointer + 1 < len(p) and p[p_pointer + 1] == '*':
            char_match = self.is_char_match(s[s_pointer], p[p_pointer])
            next_s = self.is_match_helper(s, s_pointer + 1, p, p_pointer, memo)
            next_p = self.is_match_helper(s, s_pointer, p, p_pointer + 2, memo)
            match = (char_match and next_s) or next_p

        #average case
        else:
            char_match = self.is_char_match(s[s_pointer], p[p_pointer])
            rest_match = self.is_match_helper(s, s_pointer + 1, p, p_pointer + 1, memo)
            match = char_match and rest_match

        memo[(s_pointer, p_pointer)] = match
        return match

    def is_p_valid(self, p):
        if len(p) % 2:
            return False 
        #p is x*x*x*...
        for i in range(len(p)//2):
            if p[i * 2 + 1] != '*':
                return False 
        return True 

    def is_char_match(self, s, p):
        return s == p or p == '.'
