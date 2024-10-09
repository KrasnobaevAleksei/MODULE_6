import sys
from time import sleep

class User:
    def __init__(self,
                 nickname ,
                 password ,
                 age ):
        self.nickname = nickname
        self.password = password
        self.age = age

class Video:
    def __init__(self, title : str, duration : int, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

# основной класс
class UrTube:
    def __init__(self, users = [], videos = [], current_user = User):
        self.users = users
        self.videos = videos
        self.current_user = current_user
        self.log_out()

# Вход в аккаунт проверка на совпадение логина и пароля
    def log_in(self, nickname, password):
        for i in self.users:
            if i.nickname == nickname :
                 if hash(i.password) == hash(password):
                    self.current_user = i
                    return self.current_user
                 else:
                     print("Неверный пароль")
                     break

        print('такого нет пользователя' )

# регистрация пользователя
    def register(self, nickname, password, age):
        for i in self.users:
            if i.nickname != nickname:
                continue
            else:
                return print(f"Пользователь {nickname} уже существует")
        user = User(nickname, password, age)
        self.users.append(user)
        ur.log_in(nickname, password)
        return self.users

    # обнуляем пользователя
    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            self.videos.append(i)
        return self.videos

    def get_videos(self, find_word : str):
        new_videos = []
        for i in self.videos:
            if (find_word.lower() in i.title.lower()):
                new_videos.append(i.title)
            else:
                continue
        return new_videos

    def watch_video(self, film):
        if self.current_user == None:
            return print("Войдите в аккаунт, чтобы смотреть видео")
        for i in self.videos:
            if i.adult_mode == True and self.current_user.age < 18  :
                return print("Вам нет 18 лет, пожалуйста покиньте страницу")
            if i.title == film:
                for j in range(i.duration):
                    print(j, end =" ")
                    sleep(1)
                print("Конец фильма")
            else:
                continue
    #Хеширование
    def __hash__(self):
        return hash(self.password)

if __name__ == "__main__":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user.nickname)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')


