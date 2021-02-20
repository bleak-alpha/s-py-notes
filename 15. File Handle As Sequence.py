#A file handle open for read can be treated as a string
#This string can be printed out through a loop

xfile = open('test.txt')

for text in xfile:
    print(text)


#Counting lines in a file
fhand = open('test.txt')
count = 0
for line in fhand:
    count += 1
print('Line Count: ',count)


#Entire file content can be stored in a variable by invoking read() method
fhand = open('test.txt')
strdata = fhand.read() # fhand.read() gives the content to strdata
print("Contents: ", strdata)
print("Letter count: ", len(strdata))


#startswith() object method can be used for checking whether the file string starts with given string (entered as argument in object method)
fhand = open('test.txt')
for line in fhand:
    if line.startswith('this'): print(line)


#rstrip() object can be used to remove whitespaces (i.e. \n or \t) from string
fhand = open('test.txt')
for line in fhand:
	line = line.rstrip()
	if line.startswith('This'):
		print(line)


#Using File name as an input to search the given string through it
fname = input("File Name: ")
try:
    fhand = open(fname)

except:
    print("404....") 
    quit()

query = input("Search Query: ")
count = 0

for line in fhand:
    if line.startswith(query):
        count += 1

print("'",query,"' was found",count,"times")


#Ex-7.1
#Read through a file and print the contents of the file all in upper case
try:
    fname = input("File Name:")
except:
    print("Error")
    quit()

fhand = open(fname)

for line in fhand:
    line = line.rstrip()
    print(line.upper())