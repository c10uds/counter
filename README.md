# Counter

一个简单的计数器实现，可用于计算元素出现的次数。

## 安装

```bash
pip install counter
```

## 使用示例

```python
from counter import BuggyCounter

# 创建一个计数器实例
counter = BuggyCounter("abracadabra")

# 获取特定元素的计数
print(counter['a'])  # 输出: 5

# 获取最常见的元素
print(counter.most_common(2))  # 输出: [('a', 5), ('b', 2)]

# 获取所有元素
print(list(counter.elements()))
```

## 开发

克隆仓库后，可以运行测试：

```bash
python -m unittest discover tests
```