class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_string = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        node = self.root

        for ch in word:
            if not ch in node.children:
                node.children[ch]=TrieNode()
            node = node.children[ch]
        
        node.is_end_of_string=True
    
    def search(self,word:str)->bool:
        node = self.root

        for ch in word:
            if not ch in node.children:
                return False
            node = node.children[ch]
        
        return node.is_end_of_string


def main():
    t = Trie()
    t.insert("eat")
    t.insert("eats")
    print(t.search("apple"))
    print(t.search("eat"))
    print(t.search("eatss"))
    print(t.search("eats"))

if __name__=="__main__":
    main()