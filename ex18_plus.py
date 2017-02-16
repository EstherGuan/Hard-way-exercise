#coding=utf-8
# 这是一个进行加法运算的函数
def jiafa(arg1, arg2):
    print "ans = %r" % (arg1 + arg2)

print "please input add1: " 
add1 = raw_input()
add1 = int(add1)
print "please input add2: "
add2 = raw_input()
add2 = int(add2)

jiafa(add1, add2)
