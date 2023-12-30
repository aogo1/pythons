# multi level inheritance
class Hassan:
    def __init__(self,money , land):
        self.money = money
        self.land = land
    def display(self):
        print(self.land)
        print(self.money)
class Ramzy(Hassan): 
    def __init__(self , name , house):
        self.name = name
        self.house = house
    def display(self):
        print(self.house)
        print(self.name) 

class Ahmed(Ramzy):
    def __init__(self , money , land , name , house):
        Ramzy.__init__(self,name,house)
    def display(self):
        print(self.land)
        print(self.money)
        print(self.house)
        print(self.name) 










#multiple inheritance
class Hassan:
    def __init__(self,money , land):
        self.money = money
        self.land = land
    def display(self):
        print(self.land)
        print(self.money)
class Ramzy: 
    def __init__(self , name , house):
        self.name = name
        self.house = house
    def display(self):
        print(self.house)
        print(self.name) 
        
class Ahmed(Hassan,Ramzy):
    def __init__(self , money , land , name , house):
        Hassan.__init__(self,money,land)
        Ramzy.__init__(self,name,house)
    def display(self):
        print(self.land)
        print(self.money)
        print(self.house)
        print(self.name) 
        
        
# class attributes and the instance attributes

class MyClass:
    class_attribute = "class attribute"

    def __init__(self):
        self.instance_attribute = "instance attribute"


my_instance = MyClass()
print(MyClass.class_attribute)
print(my_instance.class_attribute) 
print(my_instance.instance_attribute)






# over loading




# def add(a , b , c):
#     answer  = a + b + c
#     print(answer)
    
    
# def add(a , b):
#     answer = a + b
#     print(answer)

# add(3 , 4 , 4)
# #هنا هيطلع ايرور عشان هو بيستخدم اخر فانكشن انت كتبتها
# add(3 , 4)


# def add(a = None , b= None):
#     if a != None and b = None:
#         print(a)
#     else:
#         print(a+b)
# add(3)
# add(3 ,4)


# def add(datatype , *args):
#     if datatype == 'int':
#         answer = 0
#     if datatype == 'str':
#         answer = ""
#     for i in args :
#         answer += i
#         print(answer)
        
# add('int',3 ,4 ,5)


# from multipledispatch import dispatch
# @dispatch(int , int)
# def add(a , b):
#     print(a+b)

# @dispatch(float, float)
# def add(a , b):
#     print(a , b)
    
# add(2.5 , 3.7)
# add(4 ,5)







# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self) :
#         return f"person name {self.name} , and the age is {self.age}"
# p = person("ahmed" , 19)
# print(p)


















from abc import ABC , abstractmethod

# class polygon(ABC):
#     @abstractmethod
#     def noofsides(self):
#         pass

# class triangle(polygon):
#     def noofsides(self):
#         print("i have 3 sides")
# class pentagon(polygon):
#     def noofsides(self):
#         print("i have 5 sides")

# v  = triangle()
# v.noofsides


# def funcc():
#     return "heyyy"

# def anfunc(func):
#     return func()

# print(anfunc(funcc))
    
# def twice( y , x):
#     return y(y(y(x)))

# def mul(x):
#     return x**2
# print(twice(mul ,))


# def outterf():
#     outter = 10
#     def innerf():
#         inner = 20
#         print("inner:" , 20)
#         print("outter" , 10)
#     innerf()
# print(outterf())


