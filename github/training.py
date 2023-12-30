#name  = input("enter your name:")
#print(f"hello {name}!")

#number = int(input("enter a number:"))
#f number % 2 == 0:
#    print(f"{number} is even")
#else:
#    print(f"{number} is odd")

#for num in range (0 , 11 ,2):
#    if num == 6:
#        continue
#    print (num)

# ellist = [1 , 3 , 5 , 7 , 4 ]
# print("the length of the list is :", len(ellist))
# print("the sum of the list is :", sum(ellist))

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# number = int(input('enter a number:'))
# print('the factorial is:', factorial(number))
    


# information = {
    
#     'name' : 'ahmed' , 
#     'age' : 19 , 
#     'type' : 'monster'
#      }
# print('the type is :' , information['type'])


# with open("example.txt" , "w")as file:
#     file.write('hello file theres me makin a file with python and free palestine')
# with open("example.txt" , "r") as file:
#     data = file.read()
#     print(data)


# try:
#     num = float(input('enter the number:'))
#     result = 7/num
#     print('equal:',result)
# except ZeroDivisionError:
#     print('you cant devide by zero')
# except ValueError:
#     print('invalid number')
    
# items = []
# if len (items) == 0:  # or if items == []:
    #     print("empty list")
# else :
#     print(items)


# mylist = ['ahmed' , 'ramadan' , 'badr' , 'ali']
# print(mylist[4::-1])


# newlist = mylist
# newlist.append('yasser')
# print(newlist)
# from copy import copy
# newlist = copy(mylist)
# newlist.append('yasser')
# print(newlist[5::-1])
# print(mylist)

# num = 1
# while (num<=100):
#     print(num)
#     num+=1

# i = 0
# while (i<9):
#     i+=1
#     if i == 3:
#       print("exit")
#       continue
#     if i == 5:
#         print("exit the e")
#         break
#     print(i)

# for i in range(10):
#     if (i % 2==0):
#         continue
#     print(i) 

# x = int(input("enter a value: "))
# y = int(input("enter the second value: "))
# z = x+y
# print(z)

# def sum(x , y):
#     z = x + y
#     return z
# print(sum(7,8))

# def abs(x):
#     if x>=0:
#         return x
#     else:
#         return -x
# print(abs(-6))

# def abs(x):
#     if not isinstance(x , (int , float)):
#         raise ValueError("Input must be numeric")
#     elif x >= 0 :
#         return x
#     else:
#         return -x
# print(abs(-88))




# def person(name , age , **dic):    # (**) النجمتين دول بيحجزو ديكشيناري في المكان ده في حالة استعمالهم
#     print("name:" , name , " age:" , age , " other:" , dic )
# person("ahmed" , 66 , country = 'egypt' , city = 'tanta')


# def person(name , age , *tup , city = 'cairo' , gender):
#     print('name:' ,name ,' age:' , age ,' skills:' , tup , ' location:',city , ' gender:',gender )
# person("ahmed" , 19 , 'python' , 'java' , city= 'dubai' , gender= 'Male')

# def f2(a , b , c=0 ,*, d): #لما يكون في قيمة ديفولت و بعدها قيمة عادية لازم تفصل بينهم ب نجمه
#     print('a' , a , 'b' , b , 'c' , c , 'd' , d)
# print(f2(1 , 2 , 3 , 4))


# def f1(a , b , *args , **dic):
#     print('a' , a , 'b' , b , 'args' , args , 'dic' , dic)
# args = (1 , 2 , 3 , 4)
# dic = {"name" : 'ahmed' , "age" : 19}
# f1(1 , 2 , *args , **dic)


# def fact(n):
#     f = 1
#     for i in range(1 , n+1):
#         f = f * i
#     return f
# print(fact(5))

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(5))


# class Dog():
#     def __init__(self):
#            print('first')
#     def speak(self):
#            print('bla bla bla')
        
# d1 = Dog()
# d1.speak()



# p = round(1.61) - round(-1.61)
# print(p)



# class Dog():
#     def __init__(self , name1 , age1):
#           self.name=name1
#           self.age=age1
#           print('welcome')
#     def set(self):
#          print(self.name + ' is now sitting')
#     def roll(self):
#         print(self.name +' rolled over!')
        
# d1 = Dog('adola' , '17')
# d1.set()
# d1.roll()
# d2 = Dog('ali' , 14) 
# d2.set()
# d2.roll()

# class Employee():
#     empcount = 0
#     def __init__(self , name1 , salary1):
#         self.name = name1
#         self.salary = salary1
#         Employee.empcount += 1
#         print('the employee ',self.name,' is created')
#     def displaycount(self):
#          print('total employee %d' % Employee.empcount)
#     def displayemployee(self):
#          print('Name :', self.name, ', Salary:' , self.salary)


# emp = Employee('ahmed' , 70000)
# emp.displaycount()
# emp.displayemployee()
# emp2 = Employee('ali' , 50000)
# emp2.displaycount()
# emp2.displayemployee()

# class Parent():
#     parentattr = 100
#     def __init__(self):
#         print('call parent class')
#     def parentmethod(self):
#         print('call parent class method')
#     def setAttr(self , attr):
#         Parent.parentattr = attr
#     def getAttr(self):
#         print('parent class attribute' , Parent.parentattr)
# class Child(Parent):
#     def __init__(self):
#         print('call subclass con')
#     def childMethod(self):
#         print('child class method called')
# c = Child()
# c.childMethod()
# c.parentmethod()
# c.getAttr()
# c.setAttr(300)
# c.getAttr()


# import calendar
# cal = calendar.month(2020 , 11)
# print(cal)
# calendar.prcal(2002)


# class person():
#     def __init__(self , name1 , id1):
#         self.name = name1
#         self.id = id1
#     def hh(self):
#         print(self.name , 'hes id number is' , self.id)
# class engineer(person):
#    # def __init__(self , name1 , id1 , skill1):
#         #self.skill = skill1
#        # super().__init__(name1 , id1)
#       def black(self):
#           print(self.name , 'hes id number is' , self.id , 'and hes skill is ')
        
# class manager(person):
#     def __init__(self, name1, id1 , salary1):
#            super().__init__(name1 , id1)
#            self.salary = salary1
#     def man(self):
#         print(self.name , 'hes id number is' , self.id , 'and his salary is' , self.salary)
        
# cp = engineer("ahmed" , 20220010)
# cp.black()
#mn = manager('ali' , 20220077 , 7000)
#mn.man()



# class Food:
#     def __init__(self , name):
#         self.name = name
#         print(self.name , 'the daddy one')
#     def eat(self):
#         print('eat method from main class')
# class Apple(Food):
#     def __init__(self,name):
#         Food.__init__(self , name)
#         print(self.name , 'subclass and like that')

# #fd = Food('pizza')
# dd = Apple("ahmed")



# from collections.abc import Sequence
# class Items(Sequence):
#     def __init__(self, *values):
#         self._values = list(values)
#     def __len__(self):
#         return len(self._values)
#     def __getitem__(self , item):
#         return self._values.__getitem__(item)
# g = Items(1 , 2 , 3 , 4 , 5 , 6 , 7) 
# for i in g:
#     print (i)


# print("*****************************section***************************")



# class Customer:
#     def __init__(self,name1,balance1=1):
#         self.name = name1
#         self.balance = balance1
#         print("the name is" , self.name , "the balance is" , self.balance)
        
        
        
# cust = Customer("ahmed ramzy")


# class Customer:
#     def __init__(self):
#         print("then init method was called")
#     def __del__(self):
#         print("the del method was called")
        
# cust = Customer()
# del cust    
    
    
# class Customer:
#     def __init__(self , name , balance=0):
#         self.name = name
#         self.balance= balance
#         print("the init method called")
#     def __str__(self):
#         return 'Customer :' +str (self.name)+ 'balance '+ str(self.balance)
#     def __add__(self,other):
#         return Customer('test_Customer',self.balance + other)
    
# cust = Customer('ahmed')
# print(cust.balance)
# print(cust)

# c2 = cust + 240
# print(c2.balance)



# class Person():
#     def __init__(self , name1 , id1):
#         self.name = name1
#         self.id = id1
#         print(self.name , 'hes id number is' , self.id)
# class Engineer(Person):
#     def __init__(self , name1 , id1 , skill1=None):
#         self.skill = skill1
#         super().__init__( name1 , id1)
#     def black(self):
#         print(self.name , 'hes id number is' , self.id , 'and hes skill is ' , self.skill)

# pe = Person("ali" , 9999999)
# cp = Engineer("ahmed" , 20220010 , "python")
# cp.black()



#******************************************review************************************


a = ["ahemd" , 'ramzy' , 'hassan']
b = ["black ",'osama','bin laden']
a.extend(b)
print(a)

# class Coordinate(object):
#     def __init__(self, x, y):
#           self.x= x
#           self.y= y
        
#     def distance(self, other):
#         x_diff_sq= (self.x-other.x)**2
#         y_diff_sq= (self.y-other.y)**2
#         return (x_diff_sq + y_diff_sq)**0.5
# c = Coordinate(3,4)
# zero = Coordinate(1,1)
# print(c.distance(zero))

# class person():
#     def __init__(self , name1 , id1):
#         self.name = name1
#         self.id = id1
#     def hh(self):
#         print(self.name , 'hes id number is' , self.id)
# class engineer(person):
#     def __init__(self , name1 , id1 , skill1):
#         self.skill = skill1
#         super().__init__(name1 , id1)
#     def black(self):
#           print(self.name , 'hes id number is' , self.id , 'and hes skill is ' , self.skill)
        
# class manager(person):
#     def __init__(self, name1, id1 , salary1):
#            super().__init__(name1 , id1)
#            self.salary = salary1
#     def man(self):
#         print(self.name , 'hes id number is' , self.id , 'and his salary is' , self.salary)
        
# cp = engineer("ahmed" , 20220010 , "python")
# cp.black()
# mn = manager('ali' , 20220077 , 7000)
# mn.man()



# class A:
#     def __init__(self,x=3):
#         self._x = x 
# class B(A): 
#     def __init__(self):
#         super().__init__(5) 
#     def display(self): 
#         print(self._x)
# obj = B() 
# print(obj.display())


# class A: def __init_
# _(self): self._x = 5 class B(A): def display(self): print(self._x) def main(): obj = B() obj.display() main()


# class A: 
#  def __init__(self,x): 
#      self.x = x 
#  def count(self,x): 
#     self.x = self.x+1 
# class B(A): 
#  def __init__(self, y=0):
#      A.__init__(self, 3) 
#      self.y = y 
#  def count(self): 
#      self.y+=1 
# obj = B() 
# obj.count() 
# print(obj.x, obj.y)


# class Demo:
#     def __init__(self):
#        self.x = 1
#     def change(self):
#        self.x = 10
#        return self.x+1
# class Demo_derived(Demo):
#     def ahmed(self):
#        self.x=self.x+1
#        return self.x
# obj = Demo_derived()
# print(obj.change())


# class fruits:
#     def __init__(self):
#         self.price = 100
#         self.__bags = 5
#     def display(self):
#         print(self.__bags)
# obj=fruits()
# obj.display()

# class A:
#    def __init__(self,val1):
#       self.val=val1
#    def method_a(self):
#        return 10+self.val
 
# class B:
#     def __init__(self,val2):
#         self.val=val2
#     def method_b(self,obj):
#         return obj.method_a()+self.val
# obj1 =A(20)
# obj2 =B(30)
# print(obj2.method_b(obj1))
# class mohamed :
#     x="alaa"
#     z=5
#     def __init__(self,x,z):
#         self.x=x
#         self.z=z
# m=mohamed(2,4)
# print(m.x,m.z)        

# class MyClass: 
#     def __init__(self): 
    
#     def black(self): 
#         self.instance_attribute = "Hello" 
#     @black.setter
#     def ahmed(self, value): 
#         self.instance_attribute = value
         
# object = MyClass() 
# object.attribute = "World" 
# print(object.attribute)


# class MyClass: 
#     def __init__(self): 
#         self.__private_attribute = "Hello" 
# object = MyClass() 
# print(object.__private_attribute)


# class MyClass: 
#     def __init__(self, a): 
#         self._a = a 
#     @property 
#     def a(self): 
#         print("Getting attribute 'a'") 
#         return self._a 
#     @a.setter 
#     def a(self, value): 
#         print("Setting attribute 'a'") 
#         self._a = value 
# obj = MyClass(1) 
# obj.a = 2 
# print(obj.a)



# def function1(x):  
#     def function2(y):
#        print(y + 2)  
#        return y + 2
#     return 3 * function2(x)

    


# a = function1(3)
# help(function1)

# ints = [1, 3, 10]
 
# [[i, j] for i in ints for j in ints if i != j print(i)]


# [(x, y) for x in xrange(3) for y in xrange(x+1)]


# class MyClass: 
#     def __init__(self, a, b): 
#         self.a = a 
#         self.b = b 
#     def __str__(self): 
#         return f"MyClass(a={self.a}, b={self.b})" 
# class MyChildClass(MyClass): 
#     def __init__(self, a, b, c): 
#         super().__init__(a, b) 
#         self.c = c 
#     def __str__(self): 
#         return f"MyChildClass(a={self.a}, b={self.b}, c={self.c})" 
 
#     def my_method(): 
#         return MyClass(1, 2) 
# print(MyChildClass.my_method())
# class A: 
#     def m1(self):
#         return 20
# class B(A):
#     def m1(self):
#         return 30
#     def m2(self):
#         return 40
# class C(B):
#     def m2(self):
#         return 20
# obj1=A()
# obj2=B() 
# obj3=C()
# print(obj1.m1()+obj3.m1()+obj3.m2())


