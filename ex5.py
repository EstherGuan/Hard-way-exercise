#coding=utf-8
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.0 # inches
height_cm = height * 2.54  # 英寸和厘米的转换
weight = 180 # lbs
eyes = "Blue"
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %f inches tall." % height_cm   # %f 是浮点数格式符
print "He's %d pounds heavy" % weight
print "Actually that's not too heavy."
print "He\'s got %r eyes and %r hair." % (eyes, hair) # ex10的加分部分解释
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
age, height, weight, age + height + weight)
