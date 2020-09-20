'''
#Python Learn 4
Recursive Vs Iterative approach
Lambda/Anonymous Functions
'''

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
        x = FSerier[len(FSerier)-2]
        y = FSerier[len(FSerier)-1]
        z = x+y
        if z>=n: break
        else: FSerier.append(z)
    '''             
    if FSerier[len(FSerier)-2]+FSerier[len(FSerier)-1]>=n: #Recursive approach
        return FSerier
    else: 
        FSerier.append(FSerier[len(FSerier)-2]+FSerier[len(FSerier)-1])
        FibonaciiSeries(n,FSerier)'''
    return FSerier

x,y = 0,1
FSerier = []
FSerier.append(x)
FSerier.append(y)
FSerier = FibonaciiSeries (25,FSerier)
print("RecursiveVsIterative2=>","FiboSerier", FSerier)

#Lambda/Anonymous Functions
addition = lambda a,b:a+b #One liner function without defining the complete structure
print ("LabdaFunction1=>",addition(10,14) )
def sort_2nd_element(a): return a[1]
a = [[11,2,3],[4,15,1],[12,13,14],[71,1,5]]
a.sort(key=lambda x:x[0]) #key used to send function in argument, lambda function is copy of function. Or use: (key=sort_2nd_element)
print ("LabdaFunction2=>",a)  #x[0] means 1st element in each subset, x[1] means 1st element in each subset and so on

#f String
# __repr and __str
#Snake water gun

# *args [Passing Varying list of arguments] and **kwargs [ Passing varying Dictionary of arguments]
def Test1(Norm,*args,**DictionaryArgs):
    print("*args**akwargs==> ",Norm, "\t",type(args),type(DictionaryArgs),"\t",end = "") #Check Type args changed from list to tuple
    for i in args: print(i,end =" ")
    for key,value in DictionaryArgs.items(): print(f"Letter {key} is {value}", end = " ")
Testargs = [1,2,3,4,5,6,7,"ok"]
kwargs = {"1":"hello","2":"I","3":"Am","4":"Good"} #dict has to be either string or int else type error
NormalArgument = "NormalArgs"
Test1(NormalArgument,*Testargs,**kwargs) #Used in case arguments can be added as required and no need to define seperatly


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
    print (index+1,item,end = " ")

#################################################################################################

'''import subprocess
import sys

def install(ModuleName):
    subprocess.check_call([sys.executable, "-m", "pip", "install", ModuleName])

install("pytesseract")'''

'''import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

# Example
if __name__ == '__main__':
    install('pytesseract')'''