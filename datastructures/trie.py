
class TrieNode:
    def __init__(self):
        self.children =  {}
        self.last = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.word_list = []

    def get_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.last = True
        node.word = word

    def search(self, word):
        node = self.root
        for c in word:
          if c not in node.children:
            return None
          node = node.children[c]
        return node

    def traverse(self, node):
      for c,node in node.children.items():
           if node.last:
             self.word_list.append(node.word)
           else:
             self.traverse(node)

    def query(self, word):
        node = self.search(word)
        if node is None:
          return None

        if node.last or len(node.children) == 0:
          return word

        self.traverse(node)
        print(self.word_list)

 
def main():

    words = ["hi", "hey", "hello"]
    trie = Trie()
    for word in words:
        trie.insert(word)

    queries = ["hey", "get", "h"]
    trie.query("he")



if __name__ == "__main__":
    main()
