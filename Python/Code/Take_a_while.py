
# print
"""
r"xxx"可让字符串以原始内容输出,但末尾不能以奇数\结尾,否则解释器会认为你要转义最后一个引号

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
table.pop(0) # 删指定的索引
print(table)

# 查 使用range for 来查询

# 改
table[0] = "two"
print(table)

# 列表的元素也可以是列表,这就得到二维数组
table.append([100,200,300])
print(table)
print(table[-1][0])

"""

"""
元组Turle
元组一旦初始化,就不能更改其元素,除非元素是列表类型,也只能改列表的元素
"""
"""
tuple_1 = () # 空元组
print(type(tuple_1))
print("你好？")

turple_2 = (1,2,3,[123,456,789])
print(turple_2)
turple_2[3][2] = 752
print(turple_2)
"""

"""
条件判断 if-else
其实就是布尔值是True还是False

"""

"""
# 经典拳击手
table1 = [100,300,800,400,1,]
print(max(table1))
print(min(table1))
"""

"""
模式匹配
有序列模式
"""

"""
age = int(input("How old are you?")) # 类型转换

match age:
    case x if x < 10:
        print("Too young too simple")
    case 11 | 12 | 13 | 14 | 15| 16 :
        print("Not yet")
    case 18:
        print("Simply lovely")
    case y if y > 18:
        print("expolre your life")
    case _:
        print("You are so young with hope")
"""


"""
循环 for-in while
这两种
"""
"""
name_list = ["joe","zoe","moe"]
for name in name_list:
    print(f"Hello,{name}")

count = 3

while count :
    print("Hello,world!")
    count = count-1
"""

"""
字典: 键值对(Key-value)
键一定是不可变对象,比如字符串,整数什么的
"""
"""
info_list = {"Joe": 11,"Zoe":14,"Moe":17}
print(info_list["Joe"])

number_list = {1:"No.1",2:"No.2",3:"No.3"}
print(number_list[2])
print(f"you are here? {9 in number_list}")  # 判断键值是否在字典里的方法1,返回True或False
print(f"you are here ? {number_list.get(3,-3)}") # 方法2,利用dict的方法,可指定返回值(参数2),若存在返回对应的值

print(number_list)
number_list.pop(3)  # 删除对应键值对
print(number_list)
number_list[4] = "No.4" # 添加元素方法:直接给新键赋值即可
print(number_list)
"""

"""
集合-set
不能重复

一经添加就不能更改元素对象
set和dict的唯一区别仅在于没有存储对应的value,但是,set的原理和dict一样,所以,同样不可以放入可变对象,因为无法判断两个可变对象是否相等
"""
"""
set = {1,2,3,4,5,[1,2,3,4]}
print(type(set))
set.add(6)  # 添加
print(set)
set.remove(6)
print(set)
set[5][0] = "bye"
print(set)

"""
"""
引用和指针
变量是标签,赋值是贴标签
"""