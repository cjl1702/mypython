""""本章节讲述python列表"""

#1、定义列表
#2、如何获取列表中的第一个元素;中间的元素;最后一个元素;
#3、如何进行对列表进行排序;
#4、如何往列表中添加元素;
#5、如何删除一个元素;第N个元素;删除某个元素;


#列表用方括号[]表示
person = ['name','age','sex','weight','higher','job']

#获取第一个元素和最后一个元素
print(person)
print(person[0])
print(person[-1])

#在列表尾部添加元素
person.append('is_marray')
#在列表中插入元素(某个索引前加入值)
person.insert(1,'phone')
print(person)


#在列表中删除某个元素
del person[0]
print(person)
#删除列表末尾的元素，并返回删除的值，这样可以重新赋予新变量使用
person_filed = person.pop()
print(person_filed)
#如果在pop中添加索引值，表示弹出索引值对应的值
person_filed2 = person.pop(-1)
print(person_filed2)
print(person)

#删除higher这个元素[remove只能删除第一个指定的值，如果列表中存在多个要删除的值，就需要使用循环来判断是否删除了所有的值]
person.remove('higher')
print(person)


cars = ['bmw','audi','toyota','subaru']
#按正常顺序进行排列
cars.sort()
print(cars)
#按字母顺序相反的顺序排列
cars.sort(reverse=True)
print(cars)
#使用sorted()对列表进行临时排序,按字母顺序相反的顺序显示列表，源列表不变
cars2 = sorted(cars)
print(cars2)
print(cars)


#倒着打印列表
cars.reverse()
print(cars)

#列表长度len max() sum() min()
list_count = len(person)
print(list_count)


#循环列表
person_info = ['name','sex','job',['bmw','audi']]
print(isinstance(person_info,list))
for person in person_info:
    #判断元素里是否还有元素
    if(isinstance(person,list)):
        for info in person:
            print(info)
    else:
        print(person)

#range()函数创建数字列表
for value in range(1,5):
    print(value)

#使用range()函数创建数字列表
rang_list = list(range(1,5))
print(rang_list)


#切片：要创建切片，可指定要使用的第一个元素的索引和最后一个元素的索引+1
countrys = ['中国','美国','韩国','日本','朝鲜','俄罗斯','越南','菲律宾']

#截取美国,韩国，日本三个元素
print(countrys[1:4])

#如果没有指定第一个索引表示从列表开头开始 [中国到朝鲜]
print(countrys[:5])

#如果没有指定第二个索引，表示截取到列表末尾 [韩国到后面]
print(countrys[2:])

#负数索引返回列表末尾相应距离的元素 [俄罗斯到菲律宾]
print(countrys[-3:])

#复制列表[用切片两个索引都不加的方式即代表全部]
new_country = countrys[:]
#和countrys是同一个列表
not_new_country = countrys

print(new_country)
print(not_new_country)

#元组：用花括号表示,里面的元素不能修改但能循环，如果想修改就必须重新赋值
mobile = ('huawei','mi','apple')
for mob in mobile:
    print(mob)

mobile[0] = '华为'
print(mobile)







