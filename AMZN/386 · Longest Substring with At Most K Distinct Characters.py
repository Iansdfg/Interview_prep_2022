class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def length_of_longest_substring_k_distinct(self, s, k):
        # write your code here
        left, right = 0, 0
        max_len = 0
        char2cnt = dict()
    
        while right < len(s):
            if s[right] not in char2cnt:
                char2cnt[s[right]] = 1
            else:
                char2cnt[s[right]] += 1 

            right += 1

            while len(char2cnt) > k:
                char2cnt[s[left]] -= 1 
                if char2cnt[s[left]] == 0:
                    del char2cnt[s[left]]
                left += 1  

            max_len = max(max_len, right - left)
        

        return max_len



