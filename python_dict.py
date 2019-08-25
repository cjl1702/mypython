""""python字典使用"""
names = ['chenjl','chenjunlong','chenfei','cjl']

#列表中存在chenjl哦
while 'cjl' in names:
    names.remove('cjl')
    print('while循环中有cjl,所有就删除')


while True:
    name = input("请输入你的英文名字chenjunlong: ")
    #用int把string转换一下
    pwd  = int(input("请输入你的密码123:"))
    #注意in和and的使用
    if name in names and pwd == 123:
        print('你输入的' + name + '存在于names列表中')
        break
    elif pwd != 123:
        print('你输入的密码错误: ')
    else:
        print('用户名和密码都没填写正确')

#如果列表为空，if判断为false

dict_arr = {
    'name':'David',
    'age':28,
    'footer_size':28,
    'sex':'男',
    'iphone':'15611568910',
    'parent':{'father':'Tom','mother':'Jom','sister':'limei'},
    'video':['大染门','长安十二时辰','天龙八部']
}

#del()删除字典中的iphone
del(dict_arr['iphone'])
print(dict_arr)

#items()方法循环每一个元素
for key,value in dict_arr.items():
    print('键名: '+ key + ' 键值: '+ str(value))

#遍历字典中所有的键
for key in dict_arr.keys():
    print('遍历字典中的所有键名:'+key)

#遍历字典中的所有键值：
for value in dict_arr.values():
    print('遍历字典中所有的的键值:'+str(value))


#keys()返回字典中所有的键，返回一个列表
if 'name' not in dict_arr.keys():
    print('键名name不在dict中')
else:
    print('键名name存在dict中')


#sorted按【顺序】返回字典中的所有键
for name in sorted(dict_arr.keys()):
    print(name)


#set()函数剔除重复项
#for value in set(dict_arr.values()):
#    print(str(value))


#嵌套
for keys,values in dict_arr.items():
    if(isinstance(values,dict)):
        for key,value in values.items():
            print('二次嵌套中的键名: '+key+'嵌套中的键值: '+value)
    elif(isinstance(values,list)):
        for value in values:
            print('二次嵌套中的列表值: '+str(value))
    else:
        print('字典中的键名: '+keys+'嵌套中的键值: '+str(values))

