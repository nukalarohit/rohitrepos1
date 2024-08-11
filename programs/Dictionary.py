d={1:'rohit',2:'bobby',3:'bubby'}
print(type(d),d)
d[4]='thara'
print(d)
d[2]='sravani'
print(d)
d[2]='swami'
print(d)

#################    METHODS ###################
#UPDATE
d1={1:'rohit',2:'bobby',3:'bubby'}
d1.update({6:'ccc',2:'nukala'})
print(d1)
print()
print(d1.keys())
print(d1.items())
print(d1.values())

#pop
d2={1:'rohit',2:'bobby',3:'bubby'}
d2.pop(2)
print(d2)
d3={1:'rohit',2:'bobby',555:'bubby'}
print(d3[555])
print(d3.get(555))