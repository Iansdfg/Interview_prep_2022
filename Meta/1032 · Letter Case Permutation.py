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
        if len(path) == len(s):
            result.append(''.join(path))
            return

        if not s[index].isdigit():
            next_list = [s[index].lower(), s[index].upper()]
        else:
            next_list = [s[index]]

        for char in next_list:
            path.append(char)
            self.dfs(s, index + 1, path, result)
            path.pop()
