from abc import  ABC


# 1.	Создайте систему управления задачами с использованием классов. Реализуйте классы "Task", "Project" и "ProjectManager". Каждая задача должна содержать описание,
# статус (выполнена или нет) и срок выполнения. Проект должен включать в себя список задач и методы для добавления новой задачи, отметки задачи как выполненной и вывода списка всех задач.
class Task:
    def __init__(self,description,deadline):
        self.description = description
        self.status = False
        self.deadline = deadline

    def mark_as_done(self):
        self.status = True

    def __str__(self):
        return f"{self.description} ({'done' if self.status else 'not done'})"

class Project:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_all_task(self):
        return self.tasks

class ProjectManager:
    def __init__(self):
        self.projects = []

    def add_project(self,project):
        self.projects.append(project)

    def get_all_projects(self):
        return self.projects

task1 = Task("do task ikt-700", "2023-12-15")
task2 = Task("do task ikt-723", "2023-12-17")

project1 = Project()
project1.add_task(task1)
project1.add_task(task2)

manager = ProjectManager()
manager.add_project(project1)

print("All task:")
for project in manager.get_all_projects():
    for task in project.get_all_task():
        print(task)


task1.mark_as_done()

print("All tasks (after marking task 1 as done):")
for project in manager.get_all_projects():
    for task in project.get_all_task():
        print(task)


# 2.	Создайте систему для управления бронированием билетов в авиакомпании. Реализуйте классы "Passenger", "Ticket", "Flight" и "Airline ". Каждый пассажир должен иметь атрибуты,
# такие как имя и фамилия. Билет должен содержать информацию о пассажире и маршруте полета.
# Рейс должен включать в себя список зарезервированных билетов. Авиакомпания должна иметь методы для бронирования билета, отмены брони и отображения списка зарезервированных билетов.
class Passenger:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display_info(self):
        print(f"Passenger: {self.first_name} {self.last_name}")

class Ticket:
    def __init__(self, passenger, route):
        self.passenger = passenger
        self.route = route

    def display_info(self):
        print(f"Ticket for {self.passenger.first_name} {self.passenger.last_name}, Route: {self.route}")


class Flight:
    def __init__(self):
        self.reserved_tickets = []

    def reserve_ticket(self, ticket):
        self.reserved_tickets.append(ticket)

    def cancel_reservation(self, ticket):
        if ticket in self.reserved_tickets:
            self.reserved_tickets.remove(ticket)

    def display_reserved_tickets(self):
        print("Reserved Tickets:")
        for ticket in self.reserved_tickets:
            ticket.display_info()


class Airline:
    def __init__(self, name):
        self.name = name
        self.flights = []

    def create_flight(self):
        flight = Flight()
        self.flights.append(flight)
        return flight

    def add_ticket_to_flight(self, flight, ticket):
        flight.reserve_ticket(ticket)

    def display_flight_info(self, flight):
        print(f"Flight info for {self.name}:")
        flight.display_reserved_tickets()




airline = Airline("MyAirline")
flight1 = airline.create_flight()

passenger1 = Passenger("Stanisalu", "Laptsionak")
ticket1 = Ticket(passenger1, "Minsk to Berlin")
airline.add_ticket_to_flight(flight1, ticket1)

passenger2 = Passenger("Jane", "Smith")
ticket2 = Ticket(passenger2, "Minsk to S.Peterburg")
airline.add_ticket_to_flight(flight1, ticket2)

flight1.display_reserved_tickets()



# 3.	Создать абстрактный класс «Alive». Определить наследуемые классы – «Fox», «Rabbit» и «Plant». Лисы едят кроликов. Кролики едят растения. Растение поглощают солнечный свет. Представители каждого класса могут умереть, если достигнут определенного возраста или для них не будет еды.
# Напишите виртуальные методы поедания и определения состояния живых существа (живые или нет, в зависимости от достижения предельного возраста и наличия еды (входной параметр)).
# class Alive(ABC):
#     def some_method(self):
#         pass
#
# class Fox(Alive):
#
#
#
# class Rabbit(Alive):
#
#
# class Plant(Alive):

# Дополнительные задачи

# 4.	Разработайте программу, имитирующую работу транспортного агентства. Транспортное агентство имеет сеть филиалов в нескольких городах. Транспортировка грузов осуществляется между этими городами тремя видами транспорта: автомобильным, железнодорожным и воздушным. Любой вид транспортировки имеет стоимость единицы веса на единицу пути и скорость доставки. Воздушный транспорт можно использовать только между крупными городами, этот вид самый скоростной и самый дорогой.  Железнодорожный транспорт можно использовать между крупными и средними городами, этот вид самый дешевый. Автомобильный транспорт можно использовать между любыми городами. Заказчики через случайные промежутки времени обращаются в один из филиалов транспортного агентства с заказом на перевозку определенной массы груза и возможным пожеланием о скорости/цене доставки. Транспортное агентство организует отправку грузов одним из видов транспорта с учетом пожеланий клиента.
#
# -Доход транспортного агентства, в том числе с разбивкой по видам транспорта и городам.
# -Среднее время доставки груза, в том числе с разбивкой по видам транспорта и городам.
# -Список исполняемых заказов с возможность сортировки по городам, видам транспорта, стоимости перевозки.
