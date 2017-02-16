
prompt = "> "
print "Type your filename:" 
file_name = raw_input(prompt)
txt = open(file_name)
print "Here's your file %s" % file_name
print txt.read()
print txt.close()

print "Type the filename again:"
file_name_again = raw_input(prompt)
txt_again = open(file_name_again)
print txt_again.read()
print txt_again.close()
