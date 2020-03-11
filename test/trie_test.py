import unittest
from findWords.withTrie import findWords

class TestFindWordWithTrie(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.matrix3 = [['a','b','c'],
                        ['d','e','f'],
                        ['q','w','e']]
        self.matrix4 = [['a','b','c','p'],
                        ['d','e','f','k'],
                        ['q','w','e','h'],
                        ['z','x','c','v']]
        self.matrix5 = [['a','b','c','p','g'],
                        ['d','e','f','k','n'],
                        ['q','w','e','h','d'],
                        ['z','x','c','v','e'],
                        ['u','i','o','p','t']]
        self.words3 = ['aee','fed', 'wer', 'trd']
        self.words4 = ['aeev','zwfp', 'poer', 'erty']
        self.words5 = ['qwehd', 'cve','eev','rty','port']

    def test_matrix3(self):
        self.assertSetEqual({'aee','fed'},findWords(len(self.matrix3),self.words3,self.matrix3))
    
    def test_matrix4(self):
        self.assertSetEqual({'aeev','zwfp'},findWords(len(self.matrix4),self.words4,self.matrix4))
    
    def test_matrix5(self):
        self.assertSetEqual({'qwehd','cve','eev'},findWords(len(self.matrix5), self.words5, self.matrix5))
    

if __name__ == "__main__":
    unittest.main()