# def src_tgt(src,tgt):
#     if src==tgt:
#         print('src and tgt are equal')
#     else:
#         print('src and tgt are NOT equal')
#         return src+tgt,src-tgt,src/tgt,src*tgt
#
# x=int(input('enter src'))
# y=int(input('enter tgt'))
# sum1,minu,div,mul=src_tgt(x,y)
# print(sum1)
# print(minu)
# print(div)
# print(mul)


# def calc(*x):
#     s=0
#     for i in x:
#         s=s+i
#     print(s)
# # calc(10,20,30,40)
#
# def calc(**y):
#     print(y)
# calc(a=1,b=2,c=55,d='rohit',e=True)

# def marks(**m):
#     print(m)
#     som=0
#     for i in m.values():
#         som=som+i
#     if som<35:
#         print('fail')
#     else:
#         print('pass')
# marks(a=10,b=6)

# def greet(**gt):
#     for i in gt.values():
#         print(i,end=' ')
# greet(nam='rohit',grt='how are you')

# a=int(input('enter int'))
# b=float(input('enter float'))
# if a==int(b):
#     print('matching')
# else:
#     print('not matching')

# def fun1(num):
#     return num + 25
# print(fun1(5))
#
# a='aawaa'
# r=a[0::]
# l=a[::-1]
# if r==l:
#     print('palindrome')
# else:
# #     print('not palindrome')
# a=555
# b=str(a)
# print(b,type(b))

# c='rohit'
# d=int(c)
# print(c,type(c))

# l1={1:'roehit',2:'bob',3:'srav'}
# l2={1:'rohit',2:'bob',3:'srav'}
# if l1==l2:

#
#     print('matching')
# else:
#     print('not matching')

# t=int(input('enter table'))
# r=range(1,11)
# for i in r:
#     v=t*i
#     print(t,'*',i,'=',v)
#
# r=range(1,101)
# meven=0
# modd=0
# for i in r:
#     if i%2==0:
#         meven=meven+i
#     else:
#         modd=modd+i
# print(meven)
# print(modd)
#

# i=0
# while i<100:
#     i=i+3
#     print(i,end=' ')
#
# #
# s1={1,1,2,2,3,4,5,6}
# print(s1)
# s2={3,4,8,9}
# print(s1.difference(s2))
# print(s1.intersection(s2))
# s1.add(19)
# print(s1)

# str1='ETL Automation'
# for i in str1.lower():
#     if i in ['a','e','i','o','u']:
#         print('vowel')
#         break
#     else:
#         print('not vowel')

v={'a':7,'b':'bob'}
print(v,type(v))


def cal(**arg):
    print(arg,type(arg))
cal(a=1,b=2,c=3)