class  Dog():
    """第一次初始化Dog类"""

    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name = name
        self.age = age


    def sit(self,name):
        """定义一个sit方法"""
        print("小狗会"+self.name+'会坐下')

my_dog = Dog('小黄',20)
print(my_dog.name)

my_dog.name = '大黄'
print(my_dog.name)


###############类的继承#####################

class Car():
    """定义一个车的类"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make  = make
        self.model = model
        self.year  = year

    def get_decriptive_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

my_new_car = Car('Audi奥迪实例化Car',"A6",2016)
print(my_new_car.get_decriptive_name())


class ElectricCar(Car):
    """电动车的独特之处"""

    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)
        self.wheel_count = 2

    def car_desc(self):
        car_description = super().get_decriptive_name()
        """在子类方法中调用父类的方法"""
        return (car_description+ ' 调用子类car_desc方法获取轮子数量 ' +str(self.wheel_count))

my_first_car = ElectricCar('长城WEY继承父类实例化Car',"第五版",2019)
print(my_first_car.get_decriptive_name())
print(my_first_car.car_desc())
