class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def is_match(self, s, p):
        # write your code here
        memo = dict()
        return self.is_match_helper(s, 0, p, 0, memo)
        
    def is_match_helper(self, s, s_pointer, p, p_pointer, memo):
        if (s_pointer, p_pointer) in memo:
            return memo[(s_pointer, p_pointer)]

        #handle s empty
        if s_pointer >= len(s):
            for char in p[p_pointer:]:
                if char != '*':
                    return False
            return True  

        #handle p empty
        if p_pointer >= len(p):
            return False 

        #case with *
        if p[p_pointer] == '*':
            case_p_next = self.is_match_helper(s, s_pointer + 1, p, p_pointer, memo)
            case_s_next = self.is_match_helper(s, s_pointer, p, p_pointer + 1, memo)
            match = case_p_next or case_s_next
        else:
            #handle average case 
            char_match = self.is_char_match(s[s_pointer],p[p_pointer]) 
            rest_match = self.is_match_helper(s, s_pointer + 1, p, p_pointer + 1, memo)
            match = char_match and rest_match

        memo[(s_pointer, p_pointer)] = match
        return match

    def is_char_match(self,s,p):
        return s == p or p == '?'
