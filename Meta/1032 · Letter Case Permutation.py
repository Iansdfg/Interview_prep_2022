class Solution:
    """
    @param s: a string
    @return: return a list of strings
             we will sort your return value in output
    """
    def letter_case_permutation(self, s):
        # write your code here
        result = []
        self.dfs(s, 0, [], result)
        return result


    def dfs(self, s, index, path, result):
        if index >= len(s) and len(path) == len(s):
            result.append(''.join(path))
            return

        for i in range(index, len(s)):
            # if s[i].isdigit():
            #     path.append(s[i])
            #     self.dfs(s, i + 1, path, result)
            #     path.pop()
            # else:   
            #     for char in [s[i].lower(), s[i].upper()]:
            #         path.append(char)
            #         self.dfs(s, i + 1, path, result)
            #         path.pop()

            if not s[i].isdigit():
                next_list = [s[i].lower(), s[i].upper()]
            else:
                next_list = [s[i]]

            for char in next_list:
                    path.append(char)
                    self.dfs(s, i + 1, path, result)
                    path.pop()
