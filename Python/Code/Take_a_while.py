
# print
"""
r"xxx"可让字符串以原始内容输出，但末尾不能以奇数\结尾，否则解释器会认为你要转义最后一个引号

"""
# print(r"Hello\n")
# print(r'hello,"Bart"')
# print("""
# Seig Heil!
# YYYYY
#       SSSS
# SSSS
# """)

# print("Hello,%s,I'm %d" % ("Mike",11))

"""
逻辑运算
与 and  或 or 非 not
"""

# 列表list
# 增删查改
table = ["one","please",11,22]
print(table)
print(table[0]) # 列表下标从0开始
print(table[-1]) # 列表反向下标从-1开始
print(len(table))
print(len("Hello"))

# 增
table.append(123) # 尾增
table.insert(0,1) # 在对应索引下添加
print(table)

# 删
table.pop() # 删末尾
table.pop(0)
print(table)

# 查 使用range for 来查询

# 改
table[0] = "two"
print(table)

# 列表的元素也可以是列表，这就得到二维数组
table.append([100,200,300])
print(table)
print(table[-1][0])