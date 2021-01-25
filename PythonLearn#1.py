"""
PythonLearn#1:

Topics: 
#1 - Calculations,Comments,Escape Sequence, print, variable,datatypes,typecasting,String,list,tuple,set,dictionary
#2 - Conditional, Loops,Operator Short-If-Else Docstrings TryExcept Split, Join, File I/o , Global and Local Variables
#3 - Random Function Recursive Vs Iterative approach, Lambda/Anonymous Functions,f-String,r-string, *args and **kwargs
#4 - Time Module, DatetimeModule, Virtual Environment Installation and usage, Enumarate,Map Filter and Reduce functions

# __repr and __str
#Snake water gun

#Modes : r - read only - Default, w - write only, a - append only, t - text (used with r) - Default,
# b - Byte mode, w+ or r+ for Read and Write,  x - Create file if not exist  - Default

Errors:
IOError : if file can’t be opened
KeyboardInterrupt : when an unrequired key is pressed by the user
ValueError : when built-in function receives a wrong argument
EOFError : if End-Of-File is hit without reading any data
ImportError : if it is unable to find the module
ZeroDivisionError :Divide by Zero
except (RuntimeError, TypeError, NameError): pass

SourceUnplash for Photos
Tailwind CSS CSN then open with Code
Tailblocks - Source code

"""
##################################################################################################################
#1: Calculations,Comments,Escape Sequence, print, variable,datatypes,typecasting,String,list,tuple,set,dictionary
##################################################################################################################

#Calculations:
print("Calculation==>",50+30-20*2/3,26%10,10**2,10//3)
#Escape sequence: http://www.python-ds.com/python-3-escape-sequences/
print("Print==>","Ravish is working on working Directory") #Print with Next Line - new print and print with Tab \t - used with ,
print("Escape Char==>","Omansh is \" a good \\ boy \"OK\"",end = "") #No New line after this and Escape character for printing " \ "OK"
print("Escape Char 2==>","This is \t Very \nEscape Char 2 good \/ idea",end = ".\n") #Print with tab newline and end with . and new line
#More about prints
name = "Rahul"
a=2
b=4
a,b=b,a #INterchange
print("PrintType1==>","How is your dad working on stuff #",1 )
print("PrintType2==>","How is your dad working on #%d stuff %s" %(2,"22"), "OK")
print("PrintType3==>",f"{name} How is your dad working on #{{3}} \'To Do\' stuff") #f-Sting formatting

#Varibales Datatypes and Typecasting
a = 3 #int
b = 23.22 #Float
c = 23+1J #Complex
d = "NoOne is coming 3" #String
e,f = 20,30 #Multiple int
g = "24" #Sting for Typecaseting
print("Casting1==>",a+e,str(b)+d,f+int(g),type(c)) #Type Casting other are hex(string) oct() list() tuple() set()
print("String1==>",d,'\t',d[:],'\t',d[0:5],'\t')#[0:5] print(0->4),
print("String2==>",d[::],d[0:10:2],d[::-1]) # [::] [0:Len:1] and [0:10:2] 0->9 leaving one char if 3 then leave 2 char) d[::-1] is for reverse
print("String3==>",d.isalnum(),d.isnumeric(),type(d),d.strip(),d.replace("o","t"),d.find("i",1,len(d)),d.count("i"))
print("String4==>",d.split("i"),d.startswith("N"),d.endswith("0"),d.replace(" ","").isalnum(),d.isalpha()) #Alpha/Alphanumeric/Numeric not space

#More About variables assignment, List, tuple, set, and dictionary
defd = list(d) #List creation from Sting
h = defd #h created from defd list
h.append ("X")
defd.append("Y") #different elements added to lists
print("List1==>",'H List:',h) #Updating either h or d also updates other list/variable
print("List2==>",'Defdis:',defd)

#Tuple - #Brackets Immutable Cannot update or add i.e. #tup[5] = 6 #TypeError #tup.append(6) #AttributeError, but can be deleted Del <Tuple>
tup = (1,2,3,4,5)
tup1 = (('a',1),('b',2),('c',3)) 
tup3 = "e", "b", "c", "d"
print("Tuple1==>",tup+tup1,len(tup3),max(tup3),min(tup3),tuple(d),tup[1:3])#X=1:X<3 slicing
print("Tuple2==>","a" in tup3,("hi,")*3,tup3) 
#List - Can be updated, deleted del listM or del ListM[1]
listL = [['x',4], ['w',5]] #Square brackets
listM = ['physics', 'chemistry', 1997, 2000]
ListN = [1,44,33,23,54,87,98]
ListN[6] = 69 #Cannot do this with tuple
listL.sort() 
defd.reverse()
listM.append("Track")
listM.insert(1,2044) #Inset add at index update
print ("List3=>",listL,len(listM),defd[-2],defd[2],defd[:],defd.pop(3)) #Pop default pick max index else index can be specified
print ("List4=>",ListN,listM,max(ListN),min(ListN),listM.pop(),listM.remove('chemistry')) #Remove works with element not index no null
#Set are unordered and unindexed, cannot be printed from index, but can use For loops or In operator for checking, can adefd or remove or discard or update
sett = {'a','b','c','d','e',2} #Curly Braces, 
sett1 = set()
sett1.add(1)
sett1.add(2)#other functions like remove('c'), update('b','t')--add t and leave b as is,pop() No arguments with pop as unindexed
sett1.add(1) #set ignore duplicates, not added
print("Set1=>",sett1,sett,sett1.union(sett))#Other functions as in set theory, intersection,isdisjoint, 
#Dictionary
dictionary = dict(tup1)
dictionary1 = dict(listL)
dictionary2 = {'z':3,'x':4,'y':5}
dictionary2['66']=6
print("Dictionary1=>",tup3,'\t',tup,'\t',list(sett),'\t',dictionary)
print("Dictionary2=>",dictionary1,'\t',dictionary2,'\t')
for x,y in dictionary2.items(): print(f"Dictionary{y}==>",x,y)#printing elements of dictionary
#Exercise1: Simple dictionary with user input use dictionary2
##Userword = input("Enter Dictionary word: ")
##print (f"Meaning of {Userword} is {dictionary2[Userword]}")

#####################################################################################################
#2 - Conditional, Loops,Operator Short-If-Else Docstrings TryExcept Split, Join, File I/o , Global and Local Variables
#####################################################################################################

#If-Else-Elif can have multiple
if '3' in "Rado3tod": print('IF-ElIF=>Found')
elif '3' not in "Rado3tod": print ('IF-ElIF=>Not Found')
else: print('Not applicable')

#Loops: For While and Break Continue and Pass statements
print("Loops==>",end = "")
for letter in "Rahul is working $ on School":
    if letter == " ": continue
    elif letter == "$": break
    elif letter == "i": pass
    else: print(letter,end="*")
    print ("=",end = "")
print("\nInfiniteLoop==> ",end ="")
j = 0
while (1): #or True for infinite loop while True or while 1
    print (j,end = " ")
    j=j+5
    if j ==15: break

#Operators:
a,b,c,d,e,f=1,2,3,4,5,6
g = [1,2,3,4,5,6]
print("\nAritmetic Operator=> ",a+b,c-a,d*e,c**b,11/b,e//b,d%c) #/ gives a floting point result
print("Assignment Operator=> ","a=b")
print("Logical Operator=> ", a==b, f<e and d<=f, b>a or c>=d, d!=4)
print("Identity Operator=> ",a is b,a is not b)
print("Membership Operator=> ", a in g, b not in g)
print("Bitwise Operator=> ", a|b,a&b) #Works on bits 2=10 5 = 101

#Shorthand IfElse
print("ShortIfElse=> ","A is greater than B") if a>b else print("ShortIfElse=> ","B is greater than A")
def testtest(a,b):
    return (1 if (a==b) else 2)
t = testtest(1,1)
print ("ShortIfElse=> ",t)

#Functions and Docstring
def functionwithnoreturn():
    print ("Function1=> ", "Simple Function")
def sumof(a,b):
    """Docstring=>This is the docstring used to explain about the functions
    including anything from developer points of view """
    print("Function2=> ","This is from InsideFunction, sum is ",a+b )
    return a+b
h = sumof(a,b)
print("Function3=> ", f"Sum is {h}", functionwithnoreturn())
print("Function4=> ", sumof.__doc__,"Other built in",sum((a,b)),eval("c + b"))

#Try-Except
def divide(a,x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print(a+"Division by zero!")
    else:
        print(a+"Result is", result)
    finally:
        print(a+"Executing finally clause")
divide("TryExcept1=> ",2,1)
divide("TryExcept2=> ",2,0)

#Split and Join
import sys
s = "What are you doing? \n OK   \n   ok"
print("Split1==>", s.split()," ### ",s.splitlines()," ### ",s.split("\n")," ### ",s.split("?"))
x = "*".join(s).split()
y = "&".join(s.split()) #Took List of S splitted
print("Join1==>"," #",x," ## ",y," ### ","%".join(s.split("\n"))," ####")
x = 2
print("Join2==>","@".join(str(letter) for letter in ("rahul" if x==1 else [2,3,4])) ) #Joing with conditional generator
#Splitting a string Number and adding comma with decimal system ##Other Example
TempPASPrem3 = "1234567890"
TempPASPrem3 = ("  "+TempPASPrem3) if (len(TempPASPrem3)%3 ==1) else (" "+TempPASPrem3)
y = ",".join(TempPASPrem3[i:i+3] for i in range(0, len(TempPASPrem3),3))
print("".join(PASData[i][2].split("$")[1].split(".")[0].split(",")),"".join(PASData[i][3].split("$")[1].split(".")[0].split(",")))
TempPASPrem2 = str(int("".join("".join(PASData[i][2].split(".")[0].split(",")).split("$")))+int("".join("".join(PASData[i][3].split(".")[0].split(",")).split("$"))))

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
try:
    import random
    with open("TestTextFile1.txt","r+") as fd:
        x = random.sample(range(9),1)
        print("FileReadWrite5==>",fd.read(),fd.tell() )#if file dont exist through FileNotFound Exception, else if exist place pointer at 0 location
        fd.seek(12,0)
        fd.write(f"{x} Test1 \t Test 2") #Writes from the pointer 0 if file is newly opened else from where pointer current position, override if data already exist
        print ("FileReadWrite6==>",fd.seek(0,0), " " .join(s.strip() for s in fd.read())) #Nothing will be printed as pointer is at the last of the file updated
    with  open(r"TestTextFile2.txt","w+") as fd:
        x = random.sample(range(9),1)
        print("FileReadWrite7==>",fd.read()) # if file dont exist create a new one, else if file exist delete complete data - Nothing will be printed
        y = fd.write(f"{x} Test2 \t Test3") #Assigning varible to write statement gives the current pointer
        print("FileReadWrite8==>",fd.tell(),y,fd.seek(0),fd.read())
except Exception as e:
    print("R+W+=>","Exception Raised - ",e)

    
#Global and Local varibale
a = 29 #Global variable
def GlobalTest():
    a = 32 #Local variable to Function, if done a=a+1 errored out as a is not defined
    def GlobalTest2():
        global a
        a = a+1
    print("GlobalVariale2=>", f"Variable in #1 is {a}") #printing only local varibale a result
    GlobalTest2()
    print("GlobalVariale3=>", f"Variable in #2 is {a}") #printing only local varibale a result
print("GlobalVariale1=>", f"Variable before #1 is {a}") 
a = 33
GlobalTest()
print("GlobalVariale4=>", f"Variable after #1 is {a}") 
a+=9
print("GlobalVariale5=>", f"Variable after up is {a}") 

######################################################################################################################
#3 - Random Function Recursive Vs Iterative approach, Lambda/Anonymous Functions,f-String,r-string, *args and **kwargs
######################################################################################################################

#Random Function
import random
a = random.randint(1,100)
b = random.random() * 100
c = random.randrange(1,10,2)
d = random.sample([1,2,3,4,5],2)
e = ["rahul","ok","vishal", "amit"]
f = random.choice(e)
print("RandomNumbers=>", a,b,int(b),c,f)

##1: Recursive Vs Iterative approach, Lambda/Anonymous Functions,f-String, Time Module, DatetimeModule

#Recursive Vs Iterative approach
def FactorialCalc(n):
    #if n==1: return 1                      #Recursive approach
    #else: return n*FactorialCalc(n-1)
    fact = n
    for i in range(n-1,1,-1): fact = fact*i #Iterative approach
    return fact
Fact = FactorialCalc(7)
print("RecursiveVsIterative1=>",Fact)

def FibonaciiSeries(n,FSerier):#lastelem,lasttolastelem):
    while 1:                                          #Iterative
        z = FSerier[len(FSerier)-2]+FSerier[len(FSerier)-1]
        if z>=n: break
        else: FSerier.append(z)
    '''             
    if FSerier[len(FSerier)-2]+FSerier[len(FSerier)-1]>=n: #Recursive approach
        return FSerier
    else: 
        FSerier.append(FSerier[len(FSerier)-2]+FSerier[len(FSerier)-1])
        FibonaciiSeries(n,FSerier)'''
    return FSerier

FSerier = [0,1]
FSerier = FibonaciiSeries (25,FSerier)
print("RecursiveVsIterative2=>","FiboSerier", FSerier)

#Lambda/Anonymous Functions
addition = lambda a,b:a+b #One liner function without defining the complete structure
print ("LabdaFunction1=>",addition(10,14) )
def sort_2nd_element(a): return a[1]
a = [[11,2,3],[4,15,1],[12,13,14],[71,1,5]]
a.sort(key=lambda x:x[1]) #key used to send function in argument, lambda function is copy of function. Or use: (key=sort_2nd_element)
a.sort(key=lambda x:(x[1]+x[2]))
print ("LabdaFunction2=>",a)  #x[0] means 1st element in each subset, x[1] means 1st element in each subset and so on

#f String and r-String
FStringEg = f"He was a Nice {FSerier} and Must Approce {a}"
RStringEg = r"C:\Users\rahul.5.sharma.INCOFORGETECH\OneDrive - Coforge Limited\Work\Python\NewPDFRead" #Read Excape character "\" as Literal "\"

# *args [Passing Varying list of arguments] and **kwargs [ Passing varying Dictionary of arguments]
def Test1(Norm,*args,**DictionaryArgs):
    print("*args**akwargs==> ",Norm, "\t",type(args),type(DictionaryArgs),"\t",end = "") #Check Type args changed from list to tuple
    for i in args: print(i,end =" ")
    for key,value in DictionaryArgs.items(): print(f"Letter {key} is {value}", end = " ")
Testargs = [1,2,3,4,5,6,7,"ok"]
kwargs = {"1":"hello","2":"I","3":"Am","4":"Good"} #dict has to be either string or int else type error
NormalArgument = "NormalArgs"
Test1(NormalArgument,*Testargs,**kwargs) #Used in case arguments can be added as required and no need to define seperatly

######################################################################################################################
#4 - Time Module, DatetimeModule, Virtual Environment Installation and usage, Enumarate,Map Filter and Reduce functions
######################################################################################################################

#Time module - returns ticks since 12:00am, January 1, 1970(epoch)
import time
ticktime = time.time() #To calculate time taken to complete a task
time.sleep(1) #used in static wait
for i in range(10000): pass
print ("Time==>",time.ctime(time.time()),time.localtime(time.time()),time.asctime(time.localtime(time.time())))
print ("Time==>",f"For Loop time is {time.time()-ticktime}",time.strftime("%b %d %Y %H:%M:%S", time.localtime(time.time())))

#Datetime module
import datetime
TimeNow = datetime.datetime.now()
print("DateTime==>", f"Now {TimeNow}","Striffed time ",TimeNow.strftime("%Y-%m-%d"),f"Date {datetime.date(1988,8,30)} time {datetime.time(0,0,0)}")

#2 - Virtual Environment Installation and usage, Enumarate,Map Filter and Reduce functions

#Virtual Environment Installation and usage
''' 
[PIP install VirualENV] then execute [VirtualEnc <Name>]
<Name>\Scripts\activate if not work then [Set-ExecutionPolicy Unrestricted -Force]
once typed [activate] it will be activated and then [deactivate] to come out
requirements.txt - Packages need to run the project [pip freeze > requirements.txt]
Installing all module at once [pip install -r requirements.txt]
'''

#Enumarate function
ListTest = [1,2,3,4,5,6,7,8,9,10]
print("Enumearte1==>",end = " ")
#for i in range (0,len(ListTest),2): print(ListTest[i],end = " ")
j=1
for item in ListTest:
    if j%2 is not 0: print(item,end = " ")
    j+=1
print("\nEnumearte2==>",end = " ")
for index,item in enumerate(ListTest):
    print (index+1,item, end = " ")

#Import basics: 
# User can create his own pythin file [Set Path or place file in current directory]
# User can use functions by using Import <Filename>  then <Filename>.<Function Name>

#Main Function: 
# if __name__ == "__main__": <Code>

#Map Filter and Reduce functions
a = [1,2,3,4,5,6,7,8]
import functools
def SquareFind(x):    return x*x
def CubeFind(x):    return x*x*x
Functionlist = [SquareFind,CubeFind]
print("\nMap1==> ", list(map(str,a))) #Map used to type cast complete list element, or apply function to all elements and return list
print("Map2==> ", list(map(lambda x:x*x,a))) #Sqare all elements
for i in range(5,7):     print("Map3==> ", list(map(lambda x:x(i),Functionlist))) #Multiple functions applied for each element using Map
print("Filter==> ", list(filter(lambda x:x<5,a))) #Filter returns list with the filtered value
print("Reduce1==> ", functools.reduce(lambda x,y: y if y>x else x,a)) #Reduce list to single element, Gives Maximum Element
print("Reduce2==> ", functools.reduce(lambda x,y: x+y,a)) #Gives Sum of Elements

###########################################################################################################################
###########################################################################################################################