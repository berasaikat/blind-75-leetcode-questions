class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isWord = False
    def addWord(self, word):
        current = self
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.isWord = True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = TrieNode()
        for letter in words:
            root.addWord(letter)
        rows, cols = len(board), len(board[0])
        result, visit = set(), set()
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or
                r == rows or c == cols or
                board[r][c] not in node.children or
                (r, c) in visit):
                return
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                result.add(word)
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        return list(result)
    
a = Solution()
print(a.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))
print(a.findWords([["a","b"],["c","d"]], ["abcb"]))