class PrefixTree:

    def __init__(self):
        self.children = {}
        self.endOfWord = False
        

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = PrefixTree()
            node = node.children[c]
        node.endOfWord = True


    def search(self, word: str) -> bool:
        node = self
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.endOfWord
        
    # has to be sequential, but can start anywhere
    def startsWith(self, prefix: str) -> bool:
        node = self
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
            
        