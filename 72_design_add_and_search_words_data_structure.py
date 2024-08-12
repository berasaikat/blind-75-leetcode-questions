class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                current_node.children[letter] = TrieNode()
            current_node = current_node.children[letter]
        current_node.word = True
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(j, root):
            current_node = root
            for i in range(j, len(word)):
                current_letter = word[i]
                if current_letter == ".":
                    for child in current_node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if current_letter not in current_node.children:
                        return False
                    current_node = current_node.children[current_letter]
            return current_node.word
        return dfs(0, self.root)

trie = TrieNode()
operations = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
values = [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
expected_output = [None, None, None, None, False, True, True, True]
actual_output = []
for i in range(len(operations)):
    if operations[i] == "WordDictionary":
        word_dictionary = WordDictionary()
        actual_output.append(None)
    elif operations[i] == "addWord":
        word_dictionary.addWord(values[i][0])
        actual_output.append(None)
    elif operations[i] == "search":
        result = word_dictionary.search(values[i][0])
        actual_output.append(result)
print("Actual Output: ", actual_output)
print("Expected Output: ", expected_output)
print("Test Passed: ", actual_output == expected_output)