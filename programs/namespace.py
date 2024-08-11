a=10
b=20
# print(c)
print(globals())
print(locals())
def glob():
    c=50
    a=60
    print(b)
    print(f)
    print(globals())
    print(locals())
    def loc():
        global a,f
        print(c)
        a=100
        f=200
        print(globals())
        print(locals())
    loc()
glob()