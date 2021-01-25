'''
PythonLearn#2:

Topics:
#1 - Decorators,Class/Object,Doc string,Dictionary,String input for object,Inheritance - Single/multiple/MultiLevel,Access Specifier
#  

class DRY - DO NOT REPEAT, Class - Template/Blueprint, Object - Instance,Empty Class use pass

'''
###################################################################################################################################
#1 - Decorators,Class/Object,Doc string,Dictionary,String input for object,Inheritance - Single/multiple/MultiLevel,Access Specifier
###################################################################################################################################

#Decorators
from time import time
def decorate(functionInput):
    def NowExec(*args,**kwargs):
        StartTime = time()
        print("Decorator1 ==>",f"Hello Guys {StartTime}",end = " - ")
        functionInput(*args,**kwargs)
        print("\nDecorator1 ==>",f"Processing Done. Total time taken is {(time()-StartTime)*60}.")
    return NowExec

@decorate
def NormalFunction(*args,**kwargs):
    for ele in args:
        print(ele,end = "\t")

#Type1: decorator Function is called 
#args = ["TypeType","qsd"]
#NormalFunction = decorate(NormalFunction)
#NormalFunction(*args)

#Type2: Using @decorate at the top of the function
NormalFunction("Type2","Type3")

#Class/Object - Constructor, Class method, Static Method

class employee():
    '''Create your employee and enter details'''
    TestVariable = 8
    TotalLeaves = 20 #Class/Static variable - Any variable declared outside of a constructor
    def __init__(self,*args,**kwargs): #Constructor defination, Variable passed from object should be defined here
        if args is not None:
            self.Name = args[0]
            self.No = args[1]
            self.Salary = args[2]
            #self.Work = args[3] #Best Practice is to use kwargs in case parameters are not fixed
        if kwargs is not None:
            if "Work" in kwargs:
                self.Work = kwargs["Work"]
    
    def printName(self,*args):
        print("Object1 ==> Now printing from class => ",end = "")
        for ele in args:
            print(ele, end = '##')
        print()
    def printObjectDetails(self,objectRef):
        return f'Object{objectRef} ==> Name {self.Name}, No {self.No}, Salary {self.Salary}, Work is {self.Work}, Leaves {self.TotalLeaves}'
    
    @classmethod #cls is used for passing class in the method or can say used only with class method
    def changeLeaves(cls,newLeaves):
        cls.TotalLeaves = newLeaves

    @classmethod
    def inputFromString(cls,stringInput):
        return cls(*stringInput.split("#@")[0].split("#"),Work = stringInput.split("#@")[1] ) #passing 1st args with * to include all list and then kwards
    
    @staticmethod
    def printfibonocii(x): #Static method dont require object creation and can be used without cls or self parameter
        y,z=0,1
        print("Static1=> ",y, end =" ")
        for i in range(x):
            print (z,end = " ")
            y,z=z,y+z
        print()
        return 0


emp1 = employee("Rohan",20,"$500",Work="Business") #Using Constructor to add variable to Class
emp2 = employee("Ravish",22,"$1200",Work="Private")

'''With No Constructors, Class variables should be declared and passed as below
    emp1.Name = "Rahul"
    emp1.No = "21"
    emp1.Salary = "$600
    emp1.Work = "Business'''

print("Class1 ==>",emp1.Name,emp1.No,emp1.Work,emp1.Salary,emp1.TotalLeaves,employee.TotalLeaves)

emp1.printName("Rohan","Rahul","Sonam")

#Updating Object variables
emp1.Name = "Rahul"
emp1.TotalLeaves = 14 # As emp1 object variable is changed, changing class variable after this will not change this object leave
employee.TotalLeaves = 15 #TotalLeaves is Class variable, cannot change from here
print(emp2.printObjectDetails(2))
emp2.changeLeaves(29) #Changing Objecrt leaves from class methods. Class method called as C.F()[Class] or C().F() [instance]
print(emp2.printObjectDetails(3))
print(emp1.printObjectDetails(4)) #Changed to 14 initially hence will not pick class variable TotalLeaves

#Doc string and Dictionary for object
print("Class2 ==>",emp1.Name,emp1.No,emp1.Work,emp1.Salary,emp1.TotalLeaves,employee.TotalLeaves,emp1.__doc__,emp1.__dict__)

#Using String input passed to class method to seperate and pass arguments
emp3 = employee.inputFromString("RAJ#24#$1350#@Public") # kwargs seperated by #@
print(emp3.printObjectDetails(5))

#Static method in class
employee.printfibonocii(10)

#Inheritance

#Single Inheritance
class programmer(employee):#update this class using super and getting additional parameter from object
    def ProgrammerName(self,objectRef):
        return f"Object{objectRef}/Inherit Class Programmer ==> Name {self.Name}, No {self.No}, Salary {self.Salary}, Work is {self.Work}, Leaves {self.TotalLeaves}"

emp4 = programmer("Rant",20,"$500",Work="Programmer")
print(emp4.ProgrammerName(6)) # Calling in Programmer class
print(emp4.printObjectDetails(7)) #Calling in Employee class

#Multiple Inheritance
class player:
    TestVariable = 9
    noOfPlays = 4
    def __init__(self,name,game):
        self.name = name
        self.game = game
    def printObjectDetails(self,objectRef):
        return f'Object{objectRef} ==> Name {self.name}, No {self.game},No of Game {self.noOfPlays}'
    def printrandom(self,stoplmt):
        import random
        return random.randrange(stoplmt)
class coolProgrammer(employee,player): #Order of inherited class is important 
    TestVariable = 9 #All 3 class having same variable name, printed as (1-Inheriting class,2-1st inherited, 3 -2nd inherited)
    lang = ["C++","Python"]
    def printLanguages(self,Objref):
        return f'Object{Objref} ==> ',self.lang
emp5 = coolProgrammer("Rohit",25,"$1250",Work="Cool Programmer")
print("MultiInherit1 ==> ",emp5.printObjectDetails(8)) #Same function name in both class but Employer method is called as 1st in inherited
print("MultiInherit2 ==> ",emp5.printLanguages(8))
print("MultiInherit3 ==> ",emp5.TestVariable,emp5.noOfPlays) #emp5.game this will be errored as Player class constructer is not call as 2nd in list
print("MultiInherit4 ==> ",emp5.printrandom(6))

#Multiple Level Inheritance
#dad son grandson

#Access Specifiers 
# Public noofleaves = 12, accesible by all
# Private  __noofleaves = 12 - start with "__" printing (object._class__noofleaves) ##Name Mangling
# Protected _noofleaves = 12 - Start wth "_" Object of class and inherited class [Subclass] not others

###################################################################################################################################
#2 - 
###################################################################################################################################

'''
###################################################################################################################################
Questions - 
###################################################################################################################################
Can inherited class have its own constructer - No this is the main reason for using Inheritance
Constructer is called only once for the class inherited first
'''
