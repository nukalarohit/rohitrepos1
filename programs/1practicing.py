# # to compare integer and float
# a=4
# b=4.45
# if a==int(b):
#     print(f"yes matching {a} and {b}")
# else:
#     print(f"no not matching {a} and {int(b)}")

# # to compare integer and float
# a=10
# print('hello',' rohit',' how are you',sep='-',end='\t')
# print('hi','how are you',sep='!',end='\t')
# print(type(a),id(a),dir(a))

# str1='rohit"kumar'
# print(str1)
# str2="rohit'kumar"
# print(str2)
# str3="""select * from
# ref where rx='44'"""
# print(str3)

# # capitalize title lower upper swapcase
# str1='rohIT HOw are YOU'
# print(str1.upper())
# print(str1.lower())
# print(str1.capitalize())
# print(str1.title())
# print(str1.istitle())
# # print(str1.find('h',1))
# # print(str1.count('h',1))
#
# str1='rohit-nukala-kumar'
# print(str1.split('-'))
#
# ls=['bobby','rohit']
# str2=','.join(ls)
# print(str2)

# #   slicing
# str1='etl automation'
# str2=1234
# print(str1[0:])
# print(str1[-1:-5:-1])
# print(str1*3)
# print(type(str2))
# str2=str(str2)
# print(type(str2))

########   list
# ls=[1,2,'rohit']
# ls.extend([5,6,'bob'])
# print(ls)
# ls.insert(1,'sravani')
# print(ls)
#
# ls=[1,2,'rohit']
# ls.insert(1,'fff')
# print(ls)
# ls[3]='rambo'
# print(ls)

# tpl=(1,2,'rohit')
# print(tpl[0:2])
# print(tpl.count(2))
# print(tpl.index('rohit'))
#
# set1={1,2,3,2,3,4,'rohit','rohit','bobby','','','null','null'}
# set2={1,2,2,4,5,6,'srav','bobby'}
# print(set1)
# print(set2)
# print(set1.difference(set2))
# print(set1.intersection(set2))
#
# # print('hi','   ','how r u',sep='%',end='------')
# # print('rohit','   ','where r u',sep='%')
# #
# # print(none)
#
# a='etl testing very GOOd'
# print(a.count('e',88,134))

# src=int(input('enter sou1rce value'))
# tgt=int(input('enter tgt value'))
# if src==tgt:
#     print(f"src count{src} is equal to tgt {tgt} count")
# else:
#     print(f"src count {src} is not equal to tgt count{tgt}")

# strg='etl testing is good'
# print(strg.endswith('isd good',0))

# print('etl, testing ,id ,goof'.split(','))
#
# print(','.join({'etl', ' testing ', 'id ', 'goof'}))

# str='aavaa'
# s=str[0:len(str)+1:1]
# print(s)
# r=str[-1:-len(str)-1:-1]
# print(r)
# if s==r:
#     print('palidrome')
# else:
# #     print('not a palindrome')
#
# str='repeat'
# print((str*3))

#
#
# b=int('4')
# print(b,type(b))

# l = [1, 2, 3, True, 'rohit', 33.44]
# print(l, type(l))
# print(l[0:3], type(l[0:3]))
# l.append('bob')
# print(l)
#
# ls=[1,'rohit']
# print(ls)
# lsapp=ls.append(True)
# print("after appending",ls)
#
#
# l = [1, 2, 3, True, 'rohit', 33.44]
# l.extend('bob123True')
# print(l)
#
# v = [1, 2, 3, True, 'rohit', 33.44]
# v.append('bob')
# print(v)
#
# b = [1, 2, 3, True, 'rohit', 33.44]
# b.insert('bob',4)
# print(b)
#
# k = [1, 2, 3, True, 'rohit', 33.44]
# k.pop(3)
# print(k)
#
# d = [1, 2, 3, True, 'rohit', 33.44,'rohit']
# d.remove('rohit')
# print(d)
#
# u = [1, 2, 3, True, 'rohit', 33.44,'rohit']
# u.clear()
# print(u)

# g = [1, 2, 3, True, 'rohit', 33.44,'rohit']
# print(g[0:3])
#
# z = (1, 2, 3, True, 'rohit', 33.44,'rohit')
# print(z[0:3])
#
# g = [1, 2, 3, True, 'rohit', 33.44,'rohit']
# print(g.count(2))
# print(g.index('rohit',1,))
# g.reverse()
# # print(g)
# g.copy()
# print(g)
#
# g = (1, 2, 3, True, 'rohit', 33.44,'rohit')
# print(type(g[0:4]))

# g = {1:123, 2:444, 3:'bhanu', 4:True, 6:'rohit', 6:'rohit'}
# print(type(g))
# v=g.values()
# b=g.keys()
# print(v)
# print(b)
# print(g[1],g[2])
# g[7]='srav'
# g[0]='bob'
# print(g)
# h={5:5}
# print(h)
# k= {1:123, 2:444, 3:'bhanu', 4:True, 6:'rohit', 6:'rohit'}
# k.update({9:'pavan',55:'jeevan'})
# print(k)
# k.pop(667456)
# print(k)

# a,b,c,d=10,20,50,100
# if a!=b:
#     print('not equal')
# else:
#     print('equal')

# a=True
# b=False
# print(a and b)
# print(a or b)
# print(a>b)
# print(b>a)
#
# src=int(input('enter src:'))
# tgt=int(input('enter tgt:'))
# rpt=int(input('enter rpt:'))
# if src!=tgt or src!=rpt:
#     print('src and tgt not EQUAL')
# elif src==tgt or tgt!=rpt:
#     print('src and rpt NOT equal')
# elif src==tgt or src==rpt or tgt==rpt:
#     print ('all equal')

# a=10
# b=0
# print(a and b)
# print(a or b)
#
# a=int(input('enter A'))
# b=int(input('enter B'))
# print(id(a),id(b))
# # i=input('enter ')
# print(a is b)

# a='rohit'
# b='hello'
# c='rohit'
# print(a in b+c)

# l1=[1,2,3,4]
# l2=[1,2,3,4]
# print(l1==l2)

# num=int(input('enter number'))
# if num==1:
#     print('one')
# elif num==2:
#     print('two')
# else:
#     print('nothing')

# nam=input('name').split(',')
# if nam=='testing':
#     print('correct name')
# elif nam=='ROHIT':
#     print('now also correct')
# else:
#     print('not matching')

# nam1=input('name').split(' ')
# if 'rohit' in nam1:
#     print('correct')
# else:
#     print('not correct')

# num=int(input('enter number'))
# if num<0:
#     print('negative')
# elif num>0:
#     print('positive')
# elif num == 0:
#     print('zero')
# else:
#     print('invalid')

# age=int(input('enter age'))
# if age>18:
#     print('please vote')
# else:
#     print('NOOO VOTE')
#
# marks=int(input('enter marks: '))
# if marks>=70:
#     print('distiction')
# elif marks>=40 and marks<70:
#     print('pass')
# else:
#     print('fail')

# for i in [1,2,3,4,True,'rohit']:
#     print (i,sep=',',end=' ')

# val=int(input('enter value'))
# x=range(1,11)
# for i in x:
#     z=val*i
#     print(z,end=' ')
#
# c=0
# v=0
# r=range(1,101)
# e=[]
# o=[]
# for i in r:
#     x=i%2
#     if x==0:
#         e=e.append(i)
#     else:
#         o=o.append(i)
# #     for k in e:
#         c=c+k
#     print('even sum',c)
#     for u in o:
#         v=v+u
#     print('odd sum', v)
# meven=0
# modd=0
# l=[1,2,3,4,5,6,7,8,9]
# for i in l:
#     if i%2==0:
#         meven=meven+i
#     else:
#         modd=modd+i
# print('even',meven)
# print('odd',modd)

# str1='ge'
# for i in str1.lower():
#     if i in ('aeiou'):
#         #if i in ['a', 'e', 'i', 'o', 'u']:
#         print('vowel')
#         break
#     else:
# #         print('not vowel')
# r=range(6,19,3)
# for i in r:
#     print(i)

#
# for j in [2, 3]:
#     for i in range(1, 11):
#         u = j * i
#         print(j, '*', i, '=', j * i)


# i=0
# while i<100:
#     print(i)
#     i=i+2

# for i in range(1,11):
#     if i==8:
#         break
#     print(i)
#
# for i in range(1,11):
#     if i==8:
#         continue
#     print(i)

# def calc(a,b):
#     print('sum',a+b)
#     print('sub',a-b)
#     print('mul',a*b)
#     print('div',a/b)
# calc(10,20)
#
# print(0b101)
# print(0o10)
# print(0x1F)
# a=11
# print(ascii(a))

list1 = [1,24,43,4,5,6]
list2 = [22,33,44,55]
newlist=list1+list2
print(newlist)
newlist1=list1.extend(list2)
print(newlist1)
print("changed for the GIT practice")