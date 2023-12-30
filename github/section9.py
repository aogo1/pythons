

# def product(a, b):
# 	p = a * b
# 	print(p)




# def product(a, b, c):
# 	p = a * b*c
# 	print(p)


# product(4, 5)



# product(4, 5, 5)




# def add(datatype, *args):

# 	if datatype == 'int':
# 		answer = 0


# 	if datatype == 'str':
# 		answer = ''

# 	for x in args:

# 		answer = answer + x

# 	print(answer)
 
 
 
 
def add(datatype , *args):
    if datatype == 'int':
        answer = 0
    if datatype == 'str':
        answer = ''
    for i in args:
        answer = answer + i
    print(answer)
    
add('int' , 2 , 3)




# add('int', 5, 6)


# add('str', 'Hi ', 'Geeks')




# def add(a=None, b=None):

# 	if a != None and b == None:
# 		print(a)

# 	else:
# 		print(a+b)



# add(2, 3)

# add(2)

# def add(a=None , b=None):
#     if a != None and b == None:
#         print(a)
#     else:
#         print(a+b)
# add(3 , 5)


from multipledispatch import dispatch






@dispatch(int , int)
def add(a , b):
    result = a + b
    print(result)

@dispatch(int , int , int, )
def add(a,b,c):
    result = a+b+c
    print(result)
    
@dispatch(int , int , int , int)
def add(a , b, c ,d):
    result = a+b+c+d
    print(result)
    
add(33 , 54)
add(22 ,13,5)
add(71 , 3 , 9 ,10)