import collections
class Node:
    def __init__(self, letter=None, isTerminal=False):
        self.letter=letter
        self.children={}
        self.isTerminal=isTerminal
class Trie:
    def __init__(self):
        self.root = Node('')

    def __repr__(self):
        self.output([self.root])
        return ''

    def output(self, currentPath, indent=''):

        currentNode = currentPath[-1]
        if currentNode.isTerminal:
            word = ''.join([node.letter for node in currentPath])
            print
            indent + word
            indent += '  '
        for letter, node in sorted(currentNode.children.items()):
            self.output(currentPath[:] + [node], indent)

    def insert(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = Node(letter)
            current = current.children[letter]
        current.isTerminal = True

    def __contains__(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.isTerminal

    def getAllPrefixesOfWord(self, word):
        prefix = ''
        prefixes = []
        current = self.root
        for letter in word:
            if letter not in current.children:
                return prefixes
            current = current.children[letter]
            prefix += letter
            if current.isTerminal:
                prefixes.append(prefix)
        return prefixes


def longest_word(words):

    trie = Trie()
    queue = collections.deque()
    for word in words:
        prefixes = trie.getAllPrefixesOfWord(word)
        for prefix in prefixes:
            queue.append((word, word[len(prefix):]))
        trie.insert(word)

    # Process the queue
    longestWord = ''
    maxLength = 0
    while queue:
        word, suffix = queue.popleft()
        if suffix in trie and len(word) > maxLength:
            longestWord = word
            maxLength = len(word)
        else:
            prefixes = trie.getAllPrefixesOfWord(suffix)
            for prefix in prefixes:
                queue.append((word, suffix[len(prefix):]))

    return longestWord




f1=open("C:/Users/DELL/Downloads/DOC-20220923-WA0017..txt",'r')

words=[]

for line in f1:
    if(line[-1]=='\n'):
        words.append(line[:-1])
#last=f1.readlines()[-1]
#words[-1]=last
#print(words)
first=longest_word(words)
print(first)
words.remove(first)
second=longest_word(words)
print(second)
f1.close()



