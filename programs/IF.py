# #####################input
#
# a=int(input("enter the num ber"))
# print("value of a",a,type(a))
# ####################      IF ELSE          #########
# name=input("enter the name :")
# if name=='rohit':
#     print(name," is correct")
#     if name=='bobby':
#     print(name,'is also correct')
# else:
#     print('no name is matching')
#
# name=input('enter name')
# if name=='rohit':
#     print('yes')
# elif name=='bobby':
#     print('double yes')
# elif name=='thara':
#     print('soooper')
#
#          use case    1    #
# source=input('enter file type').lower()
# if source=='csv':
#     print('execute csv code')
# elif source=='json':
#     print('this is json code')
# else:
#     print('please check the correct file type')
#
# #          use case 2-if user enter numbers output shud be displayed in words.    #
# num=int(input('enter number: '))
# if num==1:
#     print('one')
# elif num==2:
#     print('two')
# elif num==3:
#     print('three')
# else:
#     print('not a valid number')

# usecase 3 positive or negative or zero number##
# num=int(input('enter number'))
# if num>0:
#     print('positive number')
# elif num==0 :
#     print('zero number')
# elif num<0:
#         print('negative number')
# else:
#         print('invalid number entered')

# usecase -- if above 18 eligible for vote else age ( entered ) is not eligible##
# age=int(input('enter your age'))
# if age>18:
#     print('eligible to vote')
# else:
#     print(f"age {age} is not eligible to vote")

    # usecase -- if marks >=70 grade A , if marks between 60-7- grade B, if marks <40 failed##

marks=int(input('enter marks'))
if marks>=70:
        print('grade A')
elif marks>50 and marks<60:
        print('grade B')
elif marks > 40 and marks < 50:
        print('grade C')
else:
        print('failed')