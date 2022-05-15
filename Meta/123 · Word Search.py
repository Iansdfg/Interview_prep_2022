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
                if board[row][col] == word[0]:
                    if self.dfs(board,row, col, 0, word, visited):
                        return True
        return False


    def dfs(self, board, x, y, index, word, visited):
        if index >= len(word):
            return True 

        if not self.is_valid(x, y, visited):
            return False 
        
        if board[x][y] != word[index]:
            return False 

        visited.add((x, y))
        for delta_x, delta_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_x = x + delta_x
            next_y = y + delta_y

            if self.dfs(board, next_x, next_y, index + 1, word, visited):
                return True 

        visited.remove((x, y))
        return False 

    def is_valid(self, x, y, visited):
        if x < 0 or x >= self.rows:
            return False 
        if y < 0 or y >= self.cols:
            return False 
        if (x, y) in visited:
            return False 
        return True

        
