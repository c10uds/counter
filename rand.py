import random
import sys

def get_random_number(seed):
    """
    使用给定的种子值生成一个0到3之间的随机整数
    
    参数:
        seed: 随机数生成器的种子值
        
    返回:
        一个0到3之间的随机整数
    """
    random.seed(seed)
    return random.randint(0, 3)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方法: python rand.py <种子值>")
        sys.exit(1)
    l = ["自选菜", "麻辣烫", "掉渣饼", "肉夹馍"]
    try:
        seed_value = int(sys.argv[1])
        result = get_random_number(seed_value)
        print(f"{l[result]}")
    except ValueError:
        print("错误: 种子值必须是一个整数")
        sys.exit(1)