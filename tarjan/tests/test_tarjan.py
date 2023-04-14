import unittest
import tarjan

class TestMain(unittest.TestCase):
    def test_mainExample(self):
        # see doc/example.png
        g = {1:[2],2:[1,5],3:[4],4:[3,5], 5:[6],6:[7],7:[8],8:[6,9],9:[]}
        for f in (tarjan.tarjan, tarjan.tarjan_recursive):
            res = list(map(frozenset, f(g)))
            self.assertTrue(res == list(map(frozenset,
                                [[9], [8,7,6], [5], [2,1], [4,3]])) or
                            res == list(map(frozenset,
                                [[9], [8,7,6], [5], [4,3], [2,1]])))

if __name__ == '__main__':
    unittest.main()
