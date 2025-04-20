# 完整测试代码实现

## 1. 手动测试完整代码
from collections import Counter

# 模拟有缺陷的Counter类
class BuggyCounter(Counter):
    def most_common(self, n=None):
        if n == 0:  # 注入的缺陷：n=0时返回空列表
            return []
        return super().most_common(n)

def test_counter_manually():
    print("\n=== 手动测试开始 ===")
    passed = 0
    total = 3
    
    # 测试1：基本计数功能
    try:
        c = BuggyCounter('abracadabra')
        expected = {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
        assert dict(c) == expected
        print("✅ 测试1通过: 基本计数")
        passed += 1
    except AssertionError as e:
        print(f"❌ 测试1失败: {e}")

    # 测试2：most_common正常情况
    try:
        top2 = c.most_common(2)
        assert top2 == [('a', 5), ('b', 2)]
        print("✅ 测试2通过: most_common(2)")
        passed += 1
    except AssertionError as e:
        print(f"❌ 测试2失败: {e}")

    # 测试3：注入的缺陷(n=0)
    try:
        result = c.most_common(0)
        assert result == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
        print("✅ 测试3通过: most_common(0)")
        passed += 1
    except AssertionError:
        print("❌ 测试3失败: 检测到注入的缺陷 (这是预期结果)")

    print(f"\n测试结果: {passed}/{total} 通过")
    if passed == total:
        print("⚠️ 注意：所有测试通过表示未检测到注入缺陷，请检查测试逻辑")

if __name__ == "__main__":
    test_counter_manually()