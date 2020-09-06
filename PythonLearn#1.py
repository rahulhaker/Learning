"""
PythonLearn#1:

Topics: Calculations,Comments,Escape Sequence, print, variable,datatypes,typecasting,String
list,tuple,set,dictionary,Conditional, Loops

SourceUnplash for Photos
Tailwind CSS CSN then open with Code
Tailblocks - Source code

"""
#Calculations:
print("Calculation==>",50+30-20*2/3)
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
print("Casting1==>",a+e,str(b)+d,f+int(g),c) #Type Casting other are hex(string) oct() list() tuple() set()
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
listM.insert(1,2044) #Inset add at index
print ("List3=>",listL,len(listM),defd[-2],defd[2],defd[:],defd.pop(3)) #Pop default pick max index else index can be specified
print ("List4=>",ListN,listM,max(ListN),min(ListN),listM.pop(),listM.remove('chemistry')) #Remove works with element not index no null
#Set are unordered and unindexed, cannot be printed from index, but can use For loops or In operator for checking, can adefd or remove or discard or update
sett = {'a','b','c','d','e',2} #Curly Braces, 
sett1 = set()
sett1.add(1)
sett1.add(2)#other functions like remove('c'), update('b','t')--add t and leave b as is,pop() No arguments with pop as unindexed
sett1.add(1) #set ignore duplicatea.
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
#If-Else-Elif can have multiple
if '3' in "Rado3tod": print('IF-ElIF=>Found')
elif '3' not in "Rado3tod": print ('IF-ElIF=>Not Found')
##else: print('Not applicable')
#Exercise2: Faulty calculator ** power and % for Modulo
'''a= input("Enter what you want to compute: ")
Oper = ''
if a.find("+") != -1: Oper = '+'
elif a.find("/") != -1: Oper = '/'
elif a.find("*") != -1: Oper = '*'
elif a.find("-") != -1: Oper = '-'
print(a,Oper)
Var1 = int(a[:a.find(Oper)])
Var2 =int(a[a.find(Oper)+1:])
Result = 0
if a == 45 and b == 3 and Oper == "*": Result = 555
elif a==56 and b == 9 and Oper == "+": Result = 77
elif Oper == "*": Result = Var1*Var2
elif Oper == "+": Result = Var1+Var2
elif Oper == "-": Result = Var1-Var2
elif Oper == "/": Result = int(float(Var1/Var2))
print(f'Result is {Result}',end = "\n")'''

#Loops: For While and Break Continue and Pass statements
print("Loops=>",end = "")
for letter in "Rahul is working $ on School":
    if letter == " ": continue
    elif letter == "$": break
    if letter != 'h': print(letter,end="*")
    else: pass
    print ("=",end = "")
j = 0
while (1): #or True for infinite loop
    print (j)
    j=j+5
    if j ==15: break