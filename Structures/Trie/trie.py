class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False


class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.eow = True


    def search(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False

            node = node.children[char]

        return node.eow


    def startswith(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False

            node = node.children[char]

        return True


    def delete(self, word):

        def remove(node, word, index):
            if index == len(word):
                if not node.eow:
                    return False
                
                node.eow = False
                
                return len(node.children) == 0

            char = word[index]

            if char not in node.children:
                return False

            should_delete = remove(
                node.children[char], word, index + 1
            )

            if should_delete:
                del node.children[char]

            return not node.eow and len(node.children) == 0

        remove(self.root, word, 0)



trie = Trie()

trie.insert("apple")
trie.insert("app")
trie.insert("apt")
trie.insert("bat")

print(trie.search("apple"))
print(trie.search("app"))
print(trie.search("ap"))

print(trie.startswith("ap"))
print(trie.startswith("ba"))
print(trie.startswith("cat"))

trie.delete("apple")

print(trie.search("apple"))
print(trie.search("app"))
print(trie.search("apt"))

trie.delete("app")

print(trie.search("app"))
print(trie.search("apt"))