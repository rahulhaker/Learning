'''
PythonLearn#2:
Operator Short-If-Else Function Docstrings TryExcept FileIO WorkingWithFiles
Errors:
IOError : if file can’t be opened
KeyboardInterrupt : when an unrequired key is pressed by the user
ValueError : when built-in function receives a wrong argument
EOFError : if End-Of-File is hit without reading any data
ImportError : if it is unable to find the module
ZeroDivisionError :Divide by Zero
except (RuntimeError, TypeError, NameError): pass
'''
#Operators:
a,b,c,d,e,f=1,2,3,4,5,6
g = [1,2,3,4,5,6]
print("Aritmetic Operator=> ",a+b,c-a,d*e,c**b,11/b,e//b,d%c) #/ gives a floting point result
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