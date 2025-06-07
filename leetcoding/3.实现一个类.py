"""
1、简述面向对象的编程思想
2、使用python实现一个类
3、定义一个类的属性和方法
4、实现类的继承
5、实现类的私有属性
"""
# 1、什么是面向对象
"""
面向对象是一种计算机编程架构思想，通过“对象”来组织代码和数据。
它认为世界是由各种对象组成，每个对象都是某个类（class)的一个实例
核心概念包括：
- 类class：是一个抽象的模版，定义了一组属性和方法，用来描述一类具有相同特征和行为的对象。
例如：汽车这个类，可能包含颜色、品牌等属性以及启动、加速等方法。

- 对象object：类的具体实例。
比如，我们可以根据汽车这个类 创建一个具体的对象，如一辆红色的宝马。

- 封装encapsulation：指将对象的状态信息（属性）和行为（方法）绑定在一起，并隐藏对象内部的实现细节。
只暴露必要的接口给外部使用。有助于保护数据的安全性，并简化了对外部使用者的接口。

- 继承Inheritance：允许创建新的类作为现有类的子类subcalss。子类自动拥有父类（superclass)的所有属性和方法，
还可以添加自己的特有属性和方法或重写父类的方法。
好处：提高代码的复用性和扩展性

- 多态polymorphism：同一个操作作用于不同的对象上可以有不同的解释和执行方式。在面向对象编程中，
这意味着不同类的对象可以通过相同接口调用，但是各自实现的功能可能不同。

- 抽象Abstraction：指忽略复杂现实世界中的事物的非本质特征，只关注与目的相关的特性，从而帮助我们管理复杂度。
在面向对象编程中，通常通过接口或者抽象类来实现。

面向对象编程的主要目的是提高软件开发效率、增强代码的可读性、可维护性和可扩展性，同时减少错误的发生。

"""


# 定义一个基类
class Animal:
    # 定义属性
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # 定义方法
    def speak(self):
        # 这是一个抽象方法，在子类中应该被重写
        raise NotImplementedError("子类必须实现speak()方法")

    def info(self):
        print(f"==========={self.age}===={self.name}")


# 定义一个猫，继承动物
class Cat(Animal):
    # 基础Animal，必须重写speak
    def speak(self):
        return "miaomiao~~"

    # 重写方法
    def info(self):
        print(f"+++++++++{self.name}++++++{self.age}")


class Dog(Animal):
    def speak(self):
        print("汪汪")

    def eat(self):
        print('我喜欢吃骨头')


from abc import ABC, abstractmethod


class Biganimal(ABC): # 继承ABC
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # 如果某个子类没有实现speak()，python会在实例化时报错。
    @abstractmethod
    def speak(self):
        pass

    def info(self):
        print(f"我是一只居家动物，我的名字是{self.name},我的年龄是{self.age}")


# 为鱼和羊添加私有属性
class Finsh(Biganimal):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.__breed = breed


    def speak(self):
        return "blueblue"

    def info(self):
        print(f"我是一只鱼，我的名字是{self.name},我的年龄是{self.age},我是一只{self.__breed}品种的鱼。")

    # 同样的,我们分别定义访问私有属性，和修改私有属性的方法
    def get_breed(self):
        return self.__breed

    def set_breed(self,breed):
        self.__breed = breed



# 同样的我再定义一个羊
class Sheep(Biganimal):
    # 新增私有属性
    def __init__(self,name,age,favorite_toy):
        super().__init__(name,age)
        self.__favorite_toy = favorite_toy

    def speak(self):
        return "咩咩~"

    def info(self):
        print(f"我是一只羊，我的名字是：{self.name}，我的年龄是{self.age},我最喜欢的玩具是{self.__favorite_toy}")

    # 访问私有属性
    def get_favorite_toy(self):
        return self.__favorite_toy

    # 修改私有属性
    def set_favorite_toy(self,toy):
        self.__favorite_toy = toy



a1 = Animal("未知",3)
c1 = Cat("三花",4)
d1 = Dog("旺财",5)

a1.info()
print(a1.name)
c1.info()
print(c1.speak())
print(c1.name)

d1.info()
d1.eat()
d1.speak()

f1 = Finsh("尼莫",3,"小丑鱼")
s1 = Sheep("肖恩",10,"毛球")

# 正常调用
print(f1.speak())

print(s1.speak())

f1.info()
s1.info()

print(f1.get_breed())
print(s1.get_favorite_toy())

f1.set_breed("斑点鱼")
s1.set_favorite_toy("青苔农场")

print(f"修改后 鱼的品种为 {f1.get_breed()}")
print(f"修改后 羊喜欢的玩具为 {s1.get_favorite_toy()}")
f1.info()
s1.info()

print(f1.name)

# ❌ 不推荐这样做（虽然仍可访问，但破坏封装性）
# print(f1._Finsh__breed)# 强行访问私有属性（不建议）