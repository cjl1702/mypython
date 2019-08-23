#!/usr/bin/env python
# -*- coding:utf-8 -*-

#定义gree_user函数，实现传递参数进行打印
def greet_user(username):
    print('hello '+username.title()+' ！')
    print('hello '+username+ ' !')


greet_user('cjl')


#定义get_user_info函数，实现输出
def get_user_info(username,sex='男'):
    user_info = username + sex
    return user_info

userinfo = get_user_info('cjl','男')
print(userinfo)


#根据用户输入的信息调用get_user_info()函数进行输出
while False:
    print("Please tell me your name:")
    print("(enter q at any time to quit)")

    username = input("First name: ")
    if username == 'q':
        break

    userinfo = get_user_info(username)
    print(userinfo)


#结合使用位置实参和任意数量实参 参数*toppings实现传递任意数量的实参,接收任意多的形参一定要放在最后
def make_pizza(size,*toppings):
    """概述要制作的比萨"""
    print('\n 制作一个'+str(size)+'需要各种材料：')
    for topping in toppings:
        print('_'+topping)


make_pizza(20,'肌肉')
make_pizza(30,'鸭肉','鹅肉','鸡肉','玉米','淀粉')

