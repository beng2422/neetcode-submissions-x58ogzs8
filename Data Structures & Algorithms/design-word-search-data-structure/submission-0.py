class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = ''
        self.isEnd = False

class WordDictionary:

    def __init__(self):
                self.root = TrieNode()


    def addWord(self, word: str) -> None:
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

        def rec(i, curr):

            if i>= len(word):
                return curr.isEnd
            if word[i] == '.':
                for x in curr.children.keys():
                    adds = []
                    if rec(i+1, curr.children[x]):
                        return True
                    return False
                
            if word[i] in curr.children :
                curr = curr.children[word[i]]
                return rec(i+1, curr)
            return False
        x = rec(0, curr)
        print(x)

        return x
        










