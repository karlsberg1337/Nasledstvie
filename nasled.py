#1
class Person:

    def __init__(self, name):
        self.__name = name   # имя человека

    @property # декоратор, который определяет метод свойства.
    def name(self):
        return self.__name

    def display_info(self): # метод для отображения имени человека.
        print(f"Имя: {self.__name} ") # вывод имени 
        



#2
class Employee: # Строка определяет Employee класс.

    def __init__(self, name): # метод вызывается автоматически при создании объекта класса.
        self.__name = name  # для инициализации имени сотрудника.

    @property
    def name(self):
        return self.__name # Он возвращает значение частного атрибута __name.

    def display_info(self): # метод отвечает за отображение информации о сотруднике.
        print(f"Имя: {self.__name} ")

    def work(self): # метод отвечает за отображение рабочего статуса сотрудника.
        print(f"{self.name} работает") # получение имени сотрудника,и что сотрудник работает

#3
class Person:

    def __init__(self, name): # используется для инициализации атрибутов объекта.
        self.__name = name   # Инкапсуляция: использование двойного подчеркивания, перед именем переменной

    @property # используется для определения метода как свойства
    def name(self):
        return self.__name

    def display_info(self): # для вывода имени пользователя:
        print(f"Имя: {self.__name} ")


#4
class Employee(Person): # Employee класс jн наследуется от Person класса и определяет новый метод, work

    def work(self):  # work Метод просто печатает сообщение указывает что сотрудник работает
        print(f"{self.name} работает")


p1 = Employee("Света") # создаем экземпляр Employee под названием p1(Света)
print(p1.name) # петаем значение атрибута 
p1.display_info() # вызываем метот display_info
p1.work() # и вызываем метод work

class Employee:

    def __init__(self, name): # Он возвращает значение частного атрибута __name.
        self.__name = name  # для инициализации имени сотрудника.


    @property
    def name(self): # Он возвращает значение частного атрибута __name.
        return self.__name

    def work(self): # метод отвечает за отображение рабочего статуса сотрудника.
        print(f"{self.name} работает") # получение имени сотрудника,и что сотрудник работает


class Student:

    def __init__(self, name): # Он возвращает значение частного атрибута __name.
        self.__name = name # для инициализации имени сотрудника.

    @property
    def name(self): # Он возвращает значение частного атрибута __name. 
        return self.__name

    def study(self):
        print(f"{self.name} учится") # получение имени сотрудника,и что сотрудник учится


class WorkingStudent(Employee, Student): # WorkingStudent наследуется от Еmployee,Student и перечисляет их
    pass


ws = WorkingStudent("Петя") # создает экземпляр WorkingStudent класса с именем ws
ws.work() # вызывает методы work() и study() в ws экземпляре.
ws.study()
