import unittest
from collections import Counter

# 被测类（带缺陷版本）
class BuggyCounter(Counter):
    def most_common(self, n=None):
        if n == 0:  # 注入的缺陷
            return []
        return super().most_common(n)

class TestCounter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n=== Unittest测试开始 ===")
    
    def setUp(self):
        self.counter = BuggyCounter('abracadabra')
    
    def test_basic_count(self):
        """测试基本计数功能"""
        self.assertEqual(
            dict(self.counter),
            {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
        )
    
    def test_most_common_normal(self):
        """测试most_common正常情况"""
        self.assertEqual(
            self.counter.most_common(2),
            [('a', 5), ('b', 2)]
        )
    
    def test_most_common_zero(self):
        """测试most_common(n=0)的缺陷情况"""
        with self.assertRaises(AssertionError):
            # 这个测试应该会失败，因为我们注入了缺陷
            self.assertEqual(
                len(self.counter.most_common(0)),
                5
            )
    
    def test_elements(self):
        """测试elements迭代器"""
        self.assertEqual(
            sorted(self.counter.elements()),
            sorted(['a','a','a','a','a','b','b','c','d','r','r'])
        )
    
    def tearDown(self):
        pass
    
    @classmethod
    def tearDownClass(cls):
        print("=== Unittest测试结束 ===")

def suite():
    """创建测试套件"""
    suite = unittest.TestSuite()
    suite.addTest(TestCounter('test_basic_count'))
    suite.addTest(TestCounter('test_most_common_normal'))
    suite.addTest(TestCounter('test_most_common_zero'))
    suite.addTest(TestCounter('test_elements'))
    return suite

if __name__ == '__main__':
    # 运行测试套件
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = suite()
    runner.run(test_suite)