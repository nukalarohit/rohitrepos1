# def calc(*arg):
#  # for i in arg:
#      print(arg)
# calc(10,20,30,40)

# def calc(**arg):
#  for i in arg.keys():
#      print(i)
# calc(a=10,b=20,c=30,d=40)

# def calc(**arg):
#      print(arg)
# calc(a=10,b=20,c=30,d=40)

# def greet(**gt):
#     greet_message=''
#     for i in gt.values():
#         greet_message =greet_message+"  "+i
#     return greet_message
# print(greet(nam='rohit',msg='how are you',msg1='good morning'))
#
# def def_arg(a,b,c=4,d=6):
#     print(a,b,c,d)
# def_arg(10,20,30,40)

# def display_person(*args):
#     for i in args:
#         print(i)
# display_person(name="Emma", age="25")
#
# def fun1(*data):
#     print()
# fun1(25, 75, 55)
#
# def fun1(num):
#     return num + 25
# fun1(5)
# print(num)

# def display(**kwargs):
#     for i in kwargs:
#         print(i)
#
# display(emp="Kelly", salary=9000)
#
# def outer_fun(a, b):
#     def inner_fun(c, d):
#         return c + d
#
#     return inner_fun(a, b)
#     return a
#
# result = outer_fun(5, 10)
# print(result)