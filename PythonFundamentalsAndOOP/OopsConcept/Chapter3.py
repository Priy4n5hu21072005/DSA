# Exception handling
try:
    a=10
    b=0 
    print(a/b)
except ZeroDivisionError :
    print("Divisiable by zero is not possible :" )
#Generaic Exception
except Exception as e:
    print("error",e)

 # Raise 
age =15
if age < 18:
    raise ValueError("age must be 18")