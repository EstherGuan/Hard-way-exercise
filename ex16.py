#coding=utf-8
from sys import argv

script, filename = argv

print "We're going to erase %r ." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

'''
n = "\n"
line_1 = line1 + n
line_2 = line2 + n
line_3 = line3 + n
target.write(line_1 + line_2 +line_3)
'''
# 代替上面的重复部分
print "And finally, we close it."
target.close()
 
