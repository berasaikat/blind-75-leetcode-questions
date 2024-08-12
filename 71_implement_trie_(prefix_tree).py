class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                current_node.children[letter] =  TrieNode()
            current_node = current_node.children[letter]
        current_node.end_of_word = True
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                return False
            current_node = current_node.children[letter]
        return current_node.end_of_word
    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current_node = self.root
        for letter in prefix:
            if letter not in current_node.children:
                return False
            current_node = current_node.children[letter]
        return True

trie = TrieNode()
operations = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
values = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
expected_output = [None, None, True, False, True, None, True]
actual_output = []
for i in range(len(operations)):
    if operations[i] == "Trie":
        trie = Trie()
        actual_output.append(None)
    elif operations[i] == "insert":
        trie.insert(values[i][0])
        actual_output.append(None)
    elif operations[i] == "search":
        result = trie.search(values[i][0])
        actual_output.append(result)
    elif operations[i] == "startsWith":
        result = trie.startsWith(values[i][0])
        actual_output.append(result)
print("Actual Output: ", actual_output)
print("Expected Output: ", expected_output)
print("Test Passed: ", actual_output == expected_output)
