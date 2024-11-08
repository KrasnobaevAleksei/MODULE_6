import  threading
from random import randint
from time import sleep


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.lock.locked()

    def deposit(self):

        for i in range(10):
            if self.balance >= 500:
                print(f"На балансе больше 500 р")
                if self.lock.locked():
                    self.lock.release()
            else:
                deposit = randint(50, 500)
                self.balance += deposit
                print(f"Пополнение: №{i} {deposit}. Баланс: {self.balance}")
            sleep(0.001)

    def take(self):
        for i in range(10):
            depo = randint(50, 500)
            print(f"Запрос: {depo}")
            if self.balance < depo:
                print(f"Запрос отклонён недостаточно средств")
                self.lock.acquire()
            else:
                self.balance -= depo
                print(f"Снятие: {depo}. Баланс: {self.balance}")

            sleep(0.001)

if __name__ == "__main__":
    bk = Bank()

    # Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance}')
