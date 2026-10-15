class TrieNode:
    def __init__(self):
        self.children = {}       # char → TrieNode
        self.is_end = False      # True if a word ends here


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            # If we've consumed the whole word, check if it's a valid word-end
            if i == len(word):
                return node.is_end

            ch = word[i]

            if ch == '.':
                # Try every child of the current node
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                # Regular character: go into the matching child if it exists
                if ch not in node.children:
                    return False
                return dfs(node.children[ch], i + 1)

        return dfs(self.root, 0)