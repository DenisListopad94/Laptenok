# 1.	Создать класс с двумя переменными. Добавить функцию вывода на экран и функцию изменения этих переменных. Добавить функцию, которая
# находит сумму значений этих переменных, и функцию которая находит наибольшее значение из этих двух переменных.
class Two_var:
    def __init__(self,var1,var2):
        self.var1 = var1
        self.var2 = var2

    def print(self):
        print(f"var1: {self.var1} ,var2: {self.var2}")

    def set_vars(self,var1,var2):
        self.var1 = var1
        self.var2 = var2

    def sum(self):
        return self.var1 + self.var2

    def max(self):
        return max(self.var1 , self.var2)

two_vars = Two_var(10,20)
two_vars.print()
print(two_vars.sum())
print(two_vars.max())


# 2.	Описать класс, реализующий десятичный счетчик, который может увеличивать или уменьшать свое значение на единицу в заданном диапазоне.
# Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями. Счетчик имеет два метода:
# увеличения и уменьшения, — и свойство, позволяющее получить его текущее состояние. Написать программу, демонстрирующую все возможности класса.
class Counter:
    def __init__(self, start=0,end=9):
        self.value = start
        self.start = start
        self.end = end

    def increase(self):
        if self.value < self.end:
            self.value += 1

    def decrease(self):
        if self.value > self.start:
            self.value -= 1

    def get_value(self):
        return self.value

counters =  Counter(3,5)
print(counters.get_value())
counters.increase()
print(counters.get_value())
counters.decrease()
print(counters.get_value())


# 3.	Реализуйте класс Shop. Предусмотреть возможность работы с произвольным числом продуктов, поиска продуктов по названию, добавления их в магазин
# и удаления продуктов из него.

class Shop:
    def __init__(self):
        self.products = []

    def add_product(self,product):
        self.products.append(product)

    def remove_product(self,product):
        self.products.remove(product)

    def find_product(self,name):
        for product in self.products:
            if product["name"] == name:
                return product

    def get_products(self):
        return self.products

shop = Shop()
shop.add_product({"name":"banana","price":1.0})
shop.add_product({"name":"apple","price":1.5})
shop.add_product({"name":"schokolate","price":3.0})
print(*shop.get_products(), sep="\n")
finding = shop.find_product("apple")
print(finding)
shop.remove_product(finding)
print(shop.get_products())

# 4.	Реализуйте класс MoneyBox, для работы с виртуальной копилкой. Каждая копилка имеет ограниченную вместимость,
# которая выражается целым числом – количеством монет(capacity -вместимость), которые можно положить в копилку.
# Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность добавлять монеты в копилку и узнавать,
# можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.
# Класс должен иметь следующий вид:
#
# class MoneyBox:
#     def__init__(self, capacity) :
#     #конструктор с аргументом- вместимость копилки
#     def can_add(self,v)
#     #True, если можно добавить v монет, False иначе
#     def add(self,v)
#     #положить v монет в копилку
#
# При создании копилки, число монет в ней равно 0.
# Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True.


class MoneyBox:
    def __init__(self,capactivy):
        self.capactivy = capactivy
        self.coin = 0

    def can_add(self,v):
        return self.coin + v <= self.capactivy

    def add(self,v):
        if self.can_add(v):
            self.coin += v
        else:
            raise ValueError("Not enough space in MoneyBox")

    def check_info_capactivy(self):
        return self.capactivy - self.coin

wallet = MoneyBox(100)
print(wallet.check_info_capactivy())
wallet.add(50)
print(wallet.check_info_capactivy())
wallet.add(51)
print(wallet.check_info_capactivy())



# Дополнительные задачи 
# 1.	Задача на взаимодействие между классами. Разработать систему «Интернет-магазин». Товаровед добавляет информацию о Товаре.
# Клиент делает заявку на товар, если товар есть в наличие в магазине то покупатель оплачивает товар иначе товаровед делает запрос на склад о наличии товара.
# 2.	Задача на взаимодействие между классами. Разработать систему «Вступительные экзамены».
# Абитуриент регистрируется на Факультет, сдает Экзамены. Преподаватель выставляет Оценку. Система подсчитывает средний бал и определяет Абитуриента,
# зачисленного в учебное заведение.
# 3.	Определить класс «Шахматная фигура» с ее координатами на шахматной доске, ее цветом (черный или белый),
# виртуальным методом «битья» другой фигуры, и унаследовать от него классы, соответствующие шахматным фигурам «Ферзь», «Пешка», «Конь».
# Написать виртуальные методы «битья» другой фигуры, которые принимают координаты другой фигуры и определяют,
# может ли данная  фигура «бить» фигуру с теми (принятыми) координатами.
#

