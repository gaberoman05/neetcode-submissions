class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Check each letter (if in word)
        # check for next (left, right, up, down)
            # if in word, update index and check letter
        # else backtrack to original position and update index
        def backtrack(r,c, word_idx, visited):
            # base case -> word has been found
            if word_idx == len(word):
                return True

            # base case -> checked full square
            if r >= len(board) and c >= len(board[0]):
                return False

            # decisions (letter matches)
            if board[r][c] == word[word_idx] and (r,c) not in visited:
                if word_idx == len(word) - 1:  # matched last character
                    return True
                visited.add((r,c))
                # next char left
                if c > 0:
                    if backtrack(r,c-1, word_idx+1, visited):
                        return True

                # next char right
                if c < len(board[0])-1:
                    if backtrack(r,c+1, word_idx+1, visited):
                        return True

                # next char up
                if r > 0:
                    if backtrack(r-1,c, word_idx+1, visited):
                        return True
                    
                # next char down
                if r < len(board)-1:
                    if backtrack(r+1,c, word_idx+1,visited):
                        return True
                visited.remove((r,c))
            return False

        visited = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r,c,0,visited):
                    return True
        return False

            

    