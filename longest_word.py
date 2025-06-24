#  APPROACH:
# 1. Build a Trie using all input words.
# 2. Use DFS to explore valid paths: only go deeper if current node marks the end of a valid word.
# 3. Track the longest valid word such that all its prefixes are also valid words.
# 4. When multiple candidates exist, return the lexicographically smallest one.

#  TIME COMPLEXITY: O(W)
# - W = total number of characters in all words.
# - Trie insertion: O(W)
# - DFS traversal: visits each node once: O(W)
# - String comparison/copying during DFS is bounded by total nodes.

#  SPACE COMPLEXITY: O(W)
# - Trie storage: O(W)
# - Recursion call stack (DFS): O(L), L = max word length
# - Result and path tracking: O(L), total auxiliary is still O(W)

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

class Solution:
    def longestWord(self, words: list[str]) -> str:
        tree = Trie()
        for word in words:
            tree.insert(word)
        
        res = []

        def dfs(node, path):
            nonlocal res
            if node != tree.root and not node.word:
                return
            if len(path) > len(res) or (len(path) == len(res) and path < res):
                res = path[:]
            for char in sorted(node.children.keys()):
                path.append(char)
                dfs(node.children[char], path)
                path.pop()

        dfs(tree.root, [])
        return ''.join(res)

def main():
    words = ["w","wo","wor","worl","world"]
    words2 = ["a","banana","app","appl","ap","apply","apple"]
    solution = Solution()
    print(solution.longestWord(words))
    print(solution.longestWord(words2))

if __name__ == "__main__":
    main()
