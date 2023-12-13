"""
・n進数関連のtips
【内容】
・10進数(数値)を2, 8, 16進数に変換(bin(), oct(), hex())
・n進数(文字列)を10進数に変換(n<=36)
・n進数(文字列)を10進数に変換(n>36)

"""

# 10進数 -> 2, 8, 16進数
n = 123
print(f'2進数: {bin(n)}, {type(bin(n))}')
print(f'8進数: {oct(n)}, {type(oct(n))}')
print(f'16進数: {hex(n)}, {type(hex(n))}')

# n進数 -> 10進数
# int(n, digit)で変換 -> (n: n進数文字列, digit: 何進数の文字列であるか)
# ex) 123(8進数)を10進数に変換
n = int('123', 8)
print(f'123は8進数で{n}です。{type(n)}')