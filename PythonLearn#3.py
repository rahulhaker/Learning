'''
#Python Learn 3
Split Join File I/o 

#Modes : r - read only - Default, w - write only, a - append only, t - text (used with r) - Default,
# b - Byte mode, w+ or e+ for Read and Write,  x - Create file if not exist  - Default
'''

#Split and Join
import sys
s = "What are you doing? \n OK   \n   ok"
print("Split1==>", s.split()," ### ",s.splitlines()," ### ",s.split("\n")," ### ",s.split("?"))
x = "*".join(s).split()
y = "&".join(s.split())
print("Join1==>"," #",x," ## ",y," ### ","%".join(s.split("\n"))," ####")

#File I/O
# # Readline [One line at a time] and Readlines [All]
FileHandleORFilePointer = open("TestTextFile.txt","r")
FileReader = FileHandleORFilePointer.read(5) #if no argument passed then complete file is read in string
#for line in FileHandleORFilePointer: print(line) ##: Printing Lines directly from File handle
print("FileReadWrite1==>",FileReader)  #Printed FileReader[0:5]
FileReader = FileHandleORFilePointer.read(5)  #If call again String will have data as in FileHandleORFilePointer[5:10]
print("FileReadWrite2==>", "*" .join(FileReader.split("\n")))
FileHandleORFilePointer.close()

FileHandleORFilePointer = open("TestTextFile.txt","a") #Append
FileHandleORFilePointer.write("*OK world\n")
FileHandleORFilePointer.close()
FileHandleORFilePointer1 = open("TestTextFile.txt","r")
print("FileReadWrite3==>","$" .join(line.strip() for line in FileHandleORFilePointer1)) #Printing line directly from handle
FileHandleORFilePointer1.close()

FileHandleORFilePointer = open("TestTextFile.txt","rb") # or rt for text
FileReader = FileHandleORFilePointer.read()
print("FileReadWrite4==>",FileReader)
FileHandleORFilePointer.close()

##Working  with r+ and w+ modes and with blocks
import random
with open("D:/TestTextFile1.txt","r+") as fd:
    x = random.sample(range(9),1)
    print("FileReadWrite5==>",fd.read(),fd.tell() )#if file dont exist through FileNotFound Exception, else if exist place pointer at 0 location
    fd.seek(12,0)
    fd.write(f"{x} Test1 \t Test 2") #Writes from the pointer 0 if file is newly opened else from where pointer current position, override if data already exist
    print ("FileReadWrite6==>",fd.seek(0,0), " " .join(s.strip() for s in fd.read())) #Nothing will be printed as pointer is at the last of the file updated
    fd.close()
with  open("D:/TestTextFile2.txt","w+") as fd:
    x = random.sample(range(9),1)
    print("FileReadWrite7==>",fd.read()) # if file dont exist create a new one, else if file exist delete complete data - Nothing will be printed
    y = fd.write(f"{x} Test2 \t Test3") #Assigning varible to write statement gives the current pointer
    print("FileReadWrite8==>",fd.tell(),y,fd.seek(0),fd.read())
    fd.close()
