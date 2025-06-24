# Approach:
# 1. Insert all root words from dictionary into a Trie.
# 2. For each word in the sentence:
#    - Traverse the Trie character by character.
#    - As soon as a root is matched (curr.word == True), use it to replace.
#    - If no root matches, keep the word as is.
# 3. Join the modified words to return the result.

# Time Complexity: O(M + S × L)
#     M = total characters in dictionary (Trie construction)
#     S = number of words in sentence
#     L = average length of sentence words (Trie traversal per word)

# Space Complexity: O(M + S)
#     M = space for Trie
#     S = result list

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
    
    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

class Solution:
    def replaceWords(self, dictionary, sentence):
        sentence_list = sentence.split()
        tree = Trie()
        for word in dictionary:
            tree.insert(word)
        res = []
        for word in sentence_list:
            curr = tree.root
            chars = []
            replaced = False
            for c in word:
                if c not in curr.children:
                    break
                curr = curr.children[c]
                chars.append(c)
                if curr.word:
                    res.append(''.join(chars))
                    replaced = True
                    break
            if not replaced:
                res.append(word)
        return ' '.join(res)

if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    dictionary1 = ["cat", "bat", "rat"]
    sentence1 = "the cattle was rattled by the battery"
    print(sol.replaceWords(dictionary1, sentence1))  # Output: "the cat was rat by the bat"

    # Test Case 2
    dictionary2 = ["a", "b", "c"]
    sentence2 = "aadsfasf absbs bbab cadsfafs"
    print(sol.replaceWords(dictionary2, sentence2))  # Output: "a a b c"