#file opened
fin=open('data.txt','r')
#read all lines and keep them in a string so extra lines won't be added 
content=fin.read()
# or use readlines() which will keep each lines as an element in a list
contents=fin.readlines()
#for both type of readings, each line will disappear after being read
#use loop to read lines
text=[]
for line in fin:
    #lines can also be split before stored
    text.append(line)
#close file
fin.close()



#ord chr position of each character
print(ord('a'))
print(chr(1))