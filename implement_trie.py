###
# Approach:
# We use a Trie (Prefix Tree) data structure to store and search strings efficiently.
# - Each TrieNode has a dictionary `children` to store next characters.
# - A boolean `word` marks if the node is the end of a valid word.
#
# insert(word): Traverse each character. If not in children, create new TrieNode.
#               After processing all characters, mark the last node as a word end.
#
# search(word): Traverse each character. If missing, return False.
#               At the end, return True only if `word` is True.
#
# startsWith(prefix): Traverse characters and check if the prefix exists.
#                     It doesn’t check for full word, only prefix path.
#
# Time Complexity:
# - insert/search/startsWith: O(L), where L is the length of the word or prefix.
# Space Complexity: O(N * L), N is the number of words, L is average word length.
###

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
    
    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word
    
    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

# Main function
def main():
    trie = Trie()
    print("insert('apple'):", trie.insert("apple"))  # Output: None
    print("search('apple'):", trie.search("apple"))  # Output: True
    print("search('app'):", trie.search("app"))      # Output: False
    print("startsWith('app'):", trie.startsWith("app"))  # Output: True
    print("insert('app'):", trie.insert("app"))      # Output: None
    print("search('app'):", trie.search("app"))      # Output: True

main()