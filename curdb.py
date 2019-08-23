#案例文章来源:https://juejin.im/post/5addbd0e518825671f2f62ee
#find_one_and_delete() 查找后删除
#find_one_and_update() 查找后替换
#find_one_and_replace() 查找后更新

from flask import Flask,render_template
import pymongo

#client = pymongo.MongoClient(host='localhost',port=27017)
client = pymongo.MongoClient('mongodb://localhost:27017/')

#指定数据库
db = client.python
#db = client['python']

#指定集合,相当于声明了一个collection对象
collection = db.user




#插入
student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}

#result = collection.insert(student)
#result = collection.insert([student,student2])
#插入一条数据或多条 insert,官方不建议使用insert,推荐使用insert_one,insert_many
#result = collection.insert_one(student)
#result = collection.insert_many([student,student2])
#print(result)


#find_one查询一条数据 find多条数据
result = collection.find_one({'name':'Mike'})
print(type(result))
print(result)

results = collection.find({'name':'Mike'})
print(type(results))
for result in results:
    print(result)

#根据objectId来查询，需要使用bson库里面的objectid
from bson.objectid import ObjectId
where = {'_id':ObjectId('5d464d5f71fc8e1d8ae8c951')}
result = collection.find_one(where)
print(result)

#更新update_one一条 update_all多条
condition = {'age':{'$gt':30}}
many_condition = {'age':{'$gt':20}}
result = collection.update_one(condition,{'$inc':{'age':1}})
result = collection.update_many(many_condition,{'$inc':{'age':1}})
print(result)


#删除：delete_one() delete_many()
del_condition = {'name':'陈俊龙'}
result = collection.delete_one(del_condition)
print(result)
#del_condition = {'name':'Mike'}
#results = collection.delete_many(del_condition)






