import time

#Create a TrieNode class for Trie
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

#Create Trie class
class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, char):
        return ord(char) - ord('a')

    def insert(self, key):
        pCrawl = self.root
        length = len(key)
        for i in range(length):
            index = self._charToIndex(key[i])
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
        pCrawl.isEndOfWord = True

    def search(self, key):
        pCrawl = self.root
        length = len(key)
        for i in range(length):
            index = self._charToIndex(key[i])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        return pCrawl != None and pCrawl.isEndOfWord


#Function to solve our problem, which gets N_number of width
#and height of our matrix, words lists with words, which 
#we have to find and x _ our matrix
def findWords(N, words, x):
    #create a set
    match = set()

    #create instanse of Trie
    t = Trie()

    #Insert all of the words into a trie
    for word in words:
        t.insert(word)

    #for every character of matrix we have to do the same:
    #Every character in the matrix can be a starting point of word and can have 8 directions
    #In this 8 directions there can be as many words as there is distance to the and of the matrix from this certain character
    #We check every possible word starting with the certain character and do it for all the characters and add
    #if they reside in trie, then we add it to the set. then we return the set
    for i in range(N):
        for j in range(N):
            sum1, sum2, sum3, sum4, sum5, sum6, sum7, sum8 = "", "", "", "", "", "", "", ""
            for z in range(N):
                if j < N - z:
                    sum1 += x[i][j + z]
                if i < N - z:
                    sum2 += x[i + z][j]
                if i < N - z and j < N - z:
                    sum3 += x[i + z][j + z]
                if j >= z:
                    sum4 += x[i][j - z]
                if i >= z:
                    sum5 += x[i - z][j]
                if i >= z and j >= z:
                    sum6 += x[i - z][j - z]
                if i >= z and j < N - z:
                    sum7 += x[i - z][j + z]
                if i < N - z and j >= z:
                    sum8 += x[i + z][j - z]
            
                if t.search(sum1):
                    match.add(sum1)
                if t.search(sum2):
                    match.add(sum2)
                if t.search(sum3):
                    match.add(sum3)
                if t.search(sum4):
                    match.add(sum4)
                if t.search(sum5):
                    match.add(sum5)
                if t.search(sum6):
                    match.add(sum6)
                if t.search(sum7):
                    match.add(sum7)
                if t.search(sum8):
                    match.add(sum8)
    # print(match)
    return match

#main function were we get input and summon our function
def main():

    N = int(input())
    words = list(input().split(" "))
    x = [list(input().split(" ")) for y in range(N)]
    
    findWords(N, words, x)


#check speed of our function
if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
        
        
