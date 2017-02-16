#coding=utf-8

num_aim = 9
prompt = '>'

print "Guess what i think?"
num = int(raw_input(prompt))
x = num

while x != num_aim:
    if num < num_aim:
        print "it's too small"
        num = int(raw_input(prompt))
    if num > num_aim:
        print "it's too big"
        num = int(raw_input(prompt))
    if num == num_aim:
        print "BINGO"
        x = num_aim
    

    
    
    
    

