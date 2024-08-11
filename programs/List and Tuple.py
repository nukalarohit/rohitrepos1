ls = [1, 'rohit', True, 1 + 1j, [4, 'bobby'], ('thara', 2), 23.22]
print(type(ls))
print(type(ls[2]))
print(type(ls[4]), ls[4])
print(type(ls[5]), ls[5], dir(ls))

# append
lsap1 = [1, 'hi']
print("befor appen", lsap1)
print("after append", lsap1.append(True))
print(lsap1)
print("after append", lsap1.append('thara'))
print(lsap1)
#EXTEND
lsap1.extend([1,2,3])
print('after extend',lsap1)


roh=[1,2]
print(roh)
roh.extend([4,5])
print(roh)
roh.extend(['sravani'])#add sravani as a value
print(roh)
roh.extend('sravani')# without SQUARE brackets add sravani as a single value for each alphabet
print(roh)

#INSERT
bob=[8,'rohit',33.33,True]
print(bob)
bob.insert(1,'sravani ')
print(bob)
bob.insert(0,4)
print(bob)
bob[0]='etl'
print(bob)
bob[3]='4.44'
print(bob)

#POP
bob=[8,'rohit',33.33,True,99,'bubby']
print(bob)
bob.pop()
print(bob)
bob.pop(0)
print(bob)
#REMOVE
bob=[8,'rohit',33.33,True,99,'bubby',99,55,44,55]
print(bob)
# bob.remove('bubby')
# print(bob)
# bob.remove(55)
# print(bob)
# bob.reverse()
# print(bob)
# bob.sort(reverse=True)
# print(bob)

###############       TUPLE          ############

tpl=(1,2,'bobby',True,2,3,2,3,55.66)
print(tpl[0],tpl[2:4],type(tpl[2:4]))
tpl.count(2)
print(tpl.count(2))
tpl=(1,2,'bobby',True,2,3,2,3,55.66)
print(tpl.index(3))
print(tpl.count(3))

###############       SET          ############
s={2,'bobby',True,2,3,2,3,55.66}
print(type(s),s)

ls=[1,2,2,'rohit','rohit']
print(ls)
ls=set(ls)
print(ls)
###############       SET    METHODS      ############
s1={0,1,2,3,4,4,3,5,6}
s2={3,4,4,3,5,6,7,8,9}
print(s1.difference(s2))
s1.add(8)
print(s1)