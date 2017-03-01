# +Arithmetic operators
# + - * /  //  **  %
x = 15
y = 4
print(x + y)  # 19
print(x - y)  # 11
print(x * y)  # 60
print(x / y)  # 3.75
print(x // 2)  # 7  商
print(x ** 2)  # 225  x ** y:x的y次方

# 取模: x%y,
#   若x、y符号相同取模与取余结果一样
#   若不同，取模结果和y(除数)符号相同
#   取余结果和x(被除数)符号相同
print(x % 2)  # 1  取模
print(x % -2)  # -1

# +Comparison operators
# > < == != >= <=

# +Logical operators
# and or not
x = True
y = False
# Output: x and y is False
print('x and y is', x and y)
# Output: x or y is True
print('x or y is', x or y)
# Output: not x is False
print('not x is', not x)

# +Bitwise operators
# Bitwise operators act on operands as if they were string of binary digits.
# 按位运算符作用于操作数，就好像它们是二进制数字的字符串
# It operates bit by bit, hence the name.
# 它逐位操作，因此得名
#                                       x = 10  # 0000 1010
#                                       y = 4   # 0000 0100
# &	    Bitwise AND (0&1=0)	            x& y = 0 (0000 0000)
# |	    Bitwise OR (0|1=1)	            x | y = 14 (0000 1110)
# ~	    Bitwise NOT	(0变1,1变0)          ~x = -11 (1111 0101)
# ^	    Bitwise XOR	                    x ^ y = 14 (0000 1110)
# >>	Bitwise right shift(整体右移2位)	x>> 2 = 2 (0000 0010)
# <<	Bitwise left shift(整体左移2位)	x<< 2 = 42 (0010 1000) 移几位就是x*2的几次方

# +Associativity of Python Operators
# Exponent operator ** has right-to-left associativity in Python.
# Right-left associativity of ** exponent operator
print(2 ** 3 ** 2)  # Output: 512, means 2**(3**2)

# Shows the right-left associativity
# of **
print((2 ** 3) ** 2)  # Output: 64, means 8**2

o = 1
p = 2
q = 3
print(o > p > q)  # Output: False
