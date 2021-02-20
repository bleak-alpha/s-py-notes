"""#List is a collection of various types objects under a single declaration (just like an array but can store any/all type of objects)

#using list as a for loop counter
for i in [5,4,3,2,1]:
    print(i)
print('Blast Off....')

#using range() method to generate a loop counter from list
friends = ['Joseph', 'Glenn', 'Sally']
for i in range(len(friends)):
    print("Happy New Year", friends[i])


#Ex-7.1
#Accept the numeric inputs and give out maximum and minimum
num = list() #declaring empty list by list object constructor
while True:
    elem = input("Enter a number:")
    
    if elem == 'done':
        break

    try:
        num.append(float(elem))
    except:
        print('Error,')
        continue

print('Maximum:', max(num))
print('Minimum:', min(num))
print(num)





#Ex7.3
#Spliting Sentences into words from a file and storing them in a list
while True:
    try:
        fname = input("File Name: ")
        fhand = open(fname)
    except:
        print("Error")
        continue
    break
words = fhand.read()
print(words.split())

#Ex-7.2
#Extracting senders' email id from the mailbox
email = list()

while True:
    try:
        fname = input("MailBox Name: ")
        fhand = open(fname)
    except:
        print("Error")
        continue
    break

for line in fhand:
    line = line.strip()
    wds = line.split()

    #traceback guardian for empty line
    if len(wds) < 1:
        continue

    if wds[0] != 'From': continue
    email.append(wds[1])

print(email)"""

#Ex-7.1
#Spliting words from romeo.txt
try:
    fhand = open('romeo.txt')
except:
    print("File Not Found.....")

words = list()

for line in fhand:
    line = line.strip()
    for i in range(len(line)):
        if line[i] in fhand[i]:
            words.append(line[i])
            print(words)