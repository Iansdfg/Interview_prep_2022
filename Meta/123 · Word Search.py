DIR = [(0,1), (0,-1), (1,0), (-1,0)]
class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        # write your code here
        self.rows, self.cols = len(board), len(board[0])
        visited = set()
        for row in range(self.rows):
            for col in range(self.cols):
                if self.dfs(board, row, col, word, 0, visited):
                     return True
        return False 

    def dfs(self, board, x, y, word, index, visited):
        if index >= len(word) :
            return True

        if not self.is_valid(board, x, y, word, index, visited):
            return False

        visited.add((x, y))
        for delta_x, delta_y in [(0, 1),(0, -1),(1, 0),(-1, 0)]: 
            next_x = x + delta_x
            next_y = y + delta_y
            if self.dfs(board, next_x, next_y, word, index + 1, visited):
                return True
        visited.remove((x, y))
        return False

    def is_valid(self, board, x, y, word, index, visited):
        if x < 0 or x >= self.rows:
            return False 
        if y < 0 or y >= self.cols:
            return False 
        if (x,y) in visited:
            return False 
        return board[x][y] == word[index]

        





