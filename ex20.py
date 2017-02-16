#coding=utf-8
from sys import argv                   #引进参量

script, input_file = argv              # argv 解包

def print_all(f):                      # 定义了一个函数，包含了一个参数：print_all(f)
    print f.read()                     # 函数的作用：将文件里的内容读出来 并 打印

def rewind(f):                         # 定义了一个函数，包含一个参数f：rewind()
    f.seek(0)                          # 函数的作用：从文件的第一个字节处开始

def print_a_line(line_count, f):        # 定义了一个函数，包含两个参数：print_a_line
    print line_count, f.readline()      # 函数的作用：打印行数，以及这行的内容

current_file = open(input_file)         # 将输入的文件以r模式打开。因为，文件作为参量时，只是一个字符串，是不能读入这个程序的，所以 需要 open()

print "First let's print the whole file:\n"

print_all(current_file)


print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
