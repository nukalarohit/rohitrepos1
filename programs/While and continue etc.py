# num=1
# while num<=10:
#     print(num)
#     num=num+1
# print('this is after for loop')

# roh=[1,2,'rohit',True]
# i=1
# # while i<5:
# #     print(roh[0:3])
# #     i=i+1
#
# #    BREAK
r=range(1,6)
for t in r:
    if t==3:
        break
    print(t)

print()
print()

r=range(1,6)
for t in r:
    if t==3:
        continue
    print(t)