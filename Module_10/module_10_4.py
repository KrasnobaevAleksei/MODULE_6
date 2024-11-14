import threading
import time
import random
from queue import Queue

class Table:
    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest

class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("Мы в run", threading.current_thread())
        time.sleep(random.randint(3, 10))
        print('Мы закончили')

class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.q = Queue()

    def guest_arrival(self, *guests):
        for i in range(len(self.tables)):
            self.tables[i].guest = guests[i]
            thread_1 = guests[i]
            thread_1.start()
            print(f'{guests[i].name} сел(-а) за стол номер {self.tables[i].number}')

        if len(guests) > len(self.tables):
            for i in range(len(self.tables), len(guests)):
                self.q.put(guests[i])
                print(f'{guests[i].name} в очереди')

    def discuss_guests(self):
        while not self.q.empty() :
            for table in self.tables:
                if  not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    table.guest = self.q.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    thread_1 = table.guest
                    thread_1.start()

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()