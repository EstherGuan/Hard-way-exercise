#coding=utf-8
# /：整除，%：取余，先乘除后加减，从左到右计算。不等式输出结果是真或假

print "I will now count my chickens:" # 打印这行字

print "Hens", 25.0 + 30.0 /6.0             # 公式不在引号里的就可以直接计算出结果。
print "Roosters", 100 - 25.0 * 3 % 4

print "Now I will count the eggs:"

print 3 + 2 +1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2.0 < 5 - 7                  # 不等式输出结果为真或假

print "What is 3 + 2?", 3 + 2        # 引号内的是字符串的一部分 直接打印
print "What is 5 - 7?", 5 - 7

print " Oh, taht's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?",5 <= -2
#加分题

print "result is ", 6.48 - 1.0
print 7 / 4
print 7.0 / 4.0
print 7.0 % 4.0
'''
i = 3
j = 2
k = 5
z = 7
print i + j < k - z
