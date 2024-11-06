import threading
import time


class Knight(threading.Thread):
    def __init__(self, name : str, power : int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        enemies = 100
        days_count = 0
        print(f"{self.name} на нас напали!!!")
        while enemies:
            time.sleep(1)
            days_count += 1
            enemies -= self.power
            print(f"{self.name} сражается {days_count} дней, осталось врагов {enemies}")
        print(f"{self.name} одержал победу спустя {days_count} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')