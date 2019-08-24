""""本章节讲述python基础知识"""


""""变量"""
name = "chen junlong"
age = 28
sex = 'man'

#函数title()放在变量后面，会以【首字母大写的方式】显示每个单词，
print(name)
print('每个字符串中，首字母大写：'+name.title())

#lower()函数可以将字符串转换为小写，并且存储
print('字符串中每个字母变为小写：'+name.lower())
#upper()函数可以将字符串中的每个字母变为大写
print('字符串中每个字母变为大写：'+name.upper())

#输出字符串时,如果里面有数字需要用str进行转义
age = str(age)

#拼接字符串用+
print(name+age)

#使用\t进行制表符，使用\n表示换行符
print("制表符：\t姓名"+name+"换行符：\n年龄："+age+"换行符：\n性别："+sex)

#删除字符串中的空白
# rstrip():删除字符串右侧的空白
# lstrip():删除字符串左侧的空白
# strip():删除字符串空白
long_name = ' chen   junlong  age:28  sex:man '
#print('原始拼接空格字符串:'+long_name)

long_name = long_name.rstrip()
long_name = long_name.lstrip()
long_name = long_name.strip()
print('重新赋值后才能去掉字符串中的空白：'+long_name)


