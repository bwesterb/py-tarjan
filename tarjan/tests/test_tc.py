import unittest
import tarjan.tc

class TestMain(unittest.TestCase):
    def test_mainExample(self):
        # see doc/example.png
        g = {1:[2],2:[1,5],3:[4],4:[3,5], 5:[6],6:[7],7:[8],8:[6,9],9:[]}
        res = tarjan.tc.tc(g)
        res = dict([(k, frozenset(res[k])) for k in res])
        self.assertEqual(res, {1: frozenset([1, 2, 5, 6, 7, 8, 9]),
                               2: frozenset([1, 2, 5, 6, 7, 8, 9]),
                               3: frozenset([3, 4, 5, 6, 7, 8, 9]),
                               4: frozenset([3, 4, 5, 6, 7, 8, 9]),
                               5: frozenset([8, 9, 6, 7]),
                               6: frozenset([8, 9, 6, 7]),
                               7: frozenset([8, 9, 6, 7]),
                               8: frozenset([8, 9, 6, 7]),
                               9: frozenset()})

if __name__ == '__main__':
    unittest.main()
