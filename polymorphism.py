# Task3.Week7.HOMEWORK

# 1)
'''Дан базовый класс фигур Shape. От него наследуются следующие классы Triangle, Square и
Circle.
Треугольник создаётся с заданными основанием и высотой.
Квадрат создаётся с длиной.
Круг создаётся с радиусом.
Определите в базовом классе абстрактный метод для расчёта площади, и переопределите его
в дочерних классах.
Определите функцию get_shape_area(), которая принимает фигуру и вызывает
соответствующий метод для расчёта площади.'''
# import math
# class Shape:
#     def get_shape_area(self):
#         pass

# class Triangle:
#     def __init__(self, basic, height):
#         self.basic = basic
#         self.height = height

#     def get_shape_area(self):
#         triangle_area = (self.basic * self.height) // 2 
        
#         return (f'The area of triangle is {triangle_area}')

# class Square(Shape):
#     def __init__(self, length):
#         self.lenght = length

#     def get_shape_area(self):
#         square_area = self.lenght * self.lenght
#         return (f'The area of square is {square_area}')

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def get_shape_area(self):
#         pi = math.pi
#         circle_area = pi * (self.radius * 2)
#         return(f'The area of circle is {circle_area}')

# triangle = Triangle(10, 8)
# print(triangle.get_shape_area())

# circle = Circle(2)
# print(circle.get_shape_area())

# square = Square(5)
# print(square.get_shape_area())

# 2)
'''Создайте 3 класса: Person, Employee и Student, при этом Employee и Person наследуются от
Person.
Определите в 3 классах метод get_info():
- для класса Person он должен возвращать следующее: “Привет, меня зовут Иван Петров”
- для класса Employee он должен возвращать: “Привет, меня зовут Иван Петров, я работаю в
компании “Рога и копыта” на должности “директор”
- для класса Student должно возвращаться: “Привет, меня зовут Иван Петров, я учусь в КГТУ
на 3 курсе”
Определите функцию get_human_info(), которая будет вызывать метод get_info и печатать
результат'''
# class Person:
#     def __init__(self, name, last_name):
#         self.__name = name
#         self.__last_name = last_name

#     @property
#     def name(self):
#         return self.__name
    
#     @property
#     def last_name(self):
#         return self.last_name

#     def get_info(self):
#         print(f"Hello my name is {self.__name} {self.__last_name}.")
    

# class Employee(Person):
#     def __init__(self, name, last_name, company, position):
#         super().__init__(name, last_name)
#         self.company = company
#         self.position = position

#     def get_info(self):
#         Person.get_info(self)
#         print(f"I am advirtising at {self.company} company as a best {self.position} player.")

# class Student(Person):  
#     def __init__(self, name, last_name, team, year):
#         super().__init__(name, last_name)
#         self.team = team
#         self.year = year

#     def get_info(self):
#         Person.get_info(self)
#         print(f"I played in {self.team} for {self.year} years.")

# global_ = [
#     Person('Cristiano', 'Ronaldo'),
#     Employee('Cristiano', 'Ronaldo', 'Nike', 'soccer'),
#     Student('Cristiano', 'Ronaldo', 'Real Madrid', '6')
# ]
# for people in global_:
#     people.get_info()
#     print()


# 3)
'''Создайте 2 класса: MyInt и MyString, наследуйте MyInt от int, MyString от str. У обоих
классов переопределите метод, который отвечает за работу с оператором “+”.
Напишите функцию add_objects(), которая принимает объект одного из 2 типов.
При сложении объектов класса MyInt должно выдаваться сообщение “Это сложение”, а
потом идти логика сложения 2 чисел, и выдача результата.
При конкатенации объектов класса MyString() Должно выдаваться сообщение: “Это
конкатенация”, а затем логика конкатенации из базового класса и выдача результата.'''
# class MyInt:
#     pass

# class MyString:
#     pass



















