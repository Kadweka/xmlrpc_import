import xmlrpc.client
import json


# WHERE WE GET DATA FROM
url = ""
db = ""
username = ""
password=""
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
uid = common.authenticate(db, username, password, {})
print(uid,"KADWEKA")


# WHERE WE ARE CREATING THE DATA TO
url1=""
db1=""
username1=""
password1=""
common1=xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url1))
model=xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url1))
uid1=common1.authenticate(db1, username1, password1, {})
print(uid1,"MZINGEEEEEEEEEEEEEEEEEEEEEEEEEEEE")

credit=models.execute_kw(db, uid, password,'credit.status', 'search_read', [[]], {'fields': ['name']})


total_count=0
for mgr in bussiness_stage:
    print("CREATED....",mgr)
    total_count+=1
    new_mgr=model.execute_kw(db1, uid1, password1,'business.operating.status', 'create',[mgr])
    print("TOTAL CREATED----",total_count)
