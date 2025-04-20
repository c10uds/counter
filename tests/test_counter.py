import unittest
from src.counter import BuggyCounter

class TestCounter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_data = 'abracadabra'
    
    def setUp(self):
        self.counter = BuggyCounter(self.test_data)
    
    def test_basic_counts(self):
        self.assertEqual(self.counter['a'], 5)
        self.assertEqual(self.counter['b'], 2)
    
    def test_most_common(self):
        self.assertEqual(
            self.counter.most_common(2),
            [('a', 5), ('b', 2)]
        )
    
    def test_most_common_zero(self):
        """这个测试会失败因为注入的缺陷"""
        result = self.counter.most_common(0)
        self.assertEqual(len(result), 5)  # 应该返回所有元素
    
    def test_elements(self):
        self.assertEqual(
            sorted(self.counter.elements()),
            sorted(['a']*5 + ['b']*2 + ['r']*2 + ['c','d'])
        )

if __name__ == '__main__':
    unittest.main()