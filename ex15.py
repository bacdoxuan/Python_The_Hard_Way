# Reading file

from sys import argv


script, filename = argv

txt = open(filename)

print("Here is your file: %r" % filename)
print(txt.read())

print("Type the file name again:")
file_again = input("> ")
txt_again = open(file_again)

print(txt_again.read())
