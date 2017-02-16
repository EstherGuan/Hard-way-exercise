# coding=utf-8
# 调用函数
from sys import argv

# 参数变量  这是执行命令前的参数变量
script, filename = argv

# 打开一个文件
txt = open(filename)

# 打印一行字
print "Here's your file %r:" % filename
# 打印 TXT里的内容
print txt.read()
print txt.close()

# 打印一行字
print "Type the filename again:"
'''
# 重新输入变量名 这是程序进行时的输入
file_again = raw_input("> ")

# 再一次打开文件
txt_again = open(file_again)

# 打印txt中的内容
print txt_again.read()
'''
