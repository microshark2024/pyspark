# prime.py

import math

def is_prime(n):
    """
    判断一个整数是否为素数。
    
    参数:
    n (int): 需要判断的整数。
    
    返回:
    bool: 如果 n 是素数，返回 True；否则返回 False。
    """
    # 素数必须是大于1的整数
    if n <= 1:
        return False
    
    # 2是唯一的偶数素数
    if n == 2:
        return True
    
    # 所有其他偶数都不是素数
    if n % 2 == 0:
        return False
    
    # 从3开始，检查所有奇数能否整除n
    # 我们只需要检查到 sqrt(n) 即可
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
        
    # 如果循环结束都没有找到因子，那么n是素数
    return True