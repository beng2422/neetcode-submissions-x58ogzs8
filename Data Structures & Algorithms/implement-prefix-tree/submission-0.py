class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = ''
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root

        for i in range(len(word)):
            item = word[i]
            if item in curr.children.keys():
                curr = curr.children[item]
                if i == len(word)-1:
                    curr.isEnd = True
            else:
                newVal = TrieNode()
                newVal.val = item
                if i == len(word)-1:
                    newVal.isEnd = True
                curr.children[item] = newVal
                curr = curr.children[item]



    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            if word[i] in curr.children:
                curr = curr.children[word[i]]
                if i == len(word)-1 and curr.isEnd == True:
                    return True
        return False
        

    def startsWith(self, prefix: str) -> bool:

        curr = self.root
        for i in range(len(prefix)):
            if prefix[i] in curr.children:
                curr = curr.children[prefix[i]]
                if i == len(prefix)-1:
                    return True
        return False
        










        