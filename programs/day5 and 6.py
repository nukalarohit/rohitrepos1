# a=10
# b='rohit'
# c=45.66
# d='rohit123'
# e=10
# print('type and id of a is ',type(a),id(a),end='\t')
# print('type and id  of e is ',type(e),id(e))
# print('type and id  of a is ',type(a))
# print('type and id  of a is ',type(a))
# print('type and id  of a is ',type(a))
# print('type and id  of a is ',dir(a))
#
# #Boolean
# f=True
# h=False
# print('type and id  of a is ',type(f))
# print('type and id  of a is ',type(h))
#
# #STRINGS
# print('ETL
#       'AUTOMATION')
# print("ETL 'AUTOMATION")
# print("""ETL "AUTOMATION""")
# print('''ETL AUTOMATION''')
#
# print("""select * from
# emp""")

#STRING METHODS
#----------------


str='etl testing DOMAIN'
print(str.capitalize())
print (str.title())
print(str.lower())
print(str.upper())
print(str.swapcase())
print(str.count('t',3,5))

tab1='emp'
tab2='dept'
col1='deptid'
outputval= f"""select * from {tab1} join {tab2} on
{tab1}.{col1}={tab2}.{col1}"""
print(outputval)

str9='etl testing DOMAIN'
opt=f"""output ends with MAIN: {str9.startswith('etl')}"""
print(opt)

#SPLIT
str5='rohit_nukala_kumar'
outp=str5.split('_')
print(outp,'its data type is :',type(outp))

strr='rohit!nukala!kumar'
opt=strr.split('!')
print(opt)

var=['spp_pat_id','hub_pat_id','src_key']
strv=','.join(var)
tab1='ods_spp_referral'
tab2='ods_raw_patient'
ccol='PAT_KEY'
print(f"select {strv} from {tab1} join {tab2} ON {tab1}.{ccol}={tab2}.{ccol}")
