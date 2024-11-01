
def is_prime(func):# Функция декоратор, которая принимает и возвращает функцию.
    def wrapper(*args, **kwargs):
        resulte = func(*args)
        kakoe = "Простое"
        for i in range(2, resulte - 1):
            if resulte % i == 0:
                kakoe = "Сложное"
                break
        print(kakoe)
        return resulte
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

summa = sum_three(2, 3, 6)
print(summa)