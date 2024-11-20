import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from numpy.linalg.lapack_lite import xerbla
from numpy.random.mtrand import random
import numpy.random.mtrand

########## ИСПОЛЬЗУЕМ  pandas
column_text = []
data_text = []
dictionary = {}
with open ('data.txt', encoding= 'utf - 8') as file:
    for i in file.read().split():
        n=[]
        #Проверяет состоит ли текст только из чисел.
        if i.isdigit():
            n.append(int(i))
            data_text.append(n)
        else:
            column_text.append(i)

d = dict(zip(column_text,data_text))
# Создаем таблицу с помощью pandas используя данные словаря. Ключ - название столбика, значение
df_2 = pd.DataFrame(d)
print(df_2)
# добавляем колонку с именем D и пишем в ней high если в А значение больше 5, иначе пишем low
df_2['D'] = np.where(df_2["A"] > 5, 'high', 'low')
print(df_2)
# Меняем данные столбца B если в столбце А значение меньше 5
df_2.loc[df_2.A < 5, "B" ] = 0
print(df_2)

##########  ИСПОЛЬЗУЕМ matplotlib ##########

# создаем поле с размерами на котором будет находиться наши фигурки
fig, ax = plt.subplots(figsize=(5, 2.7))
# списки с координатами
data1 = [random() for i in range(100) ]
data2 = [random() for i in range(100) ]
data3 = [random() for i in range(100) ]
data4 = [random() for i in range(100) ]
# Создаем маркеры
ax.plot( data1,'o', label='data1')
ax.plot( data2,'d', label='data2')
ax.plot( data3,'v', label='data3')
ax.plot( data4,'s', label='data4')
# легенда будет сверху справа
ax.legend(loc='upper right')
# выводим на экран
plt.show()

fig2, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
categories = ['turnips', 'rutabaga', 'cucumber', 'pumpkins']

# создаем графики в виде колон с названиями которые берем из списка categories и размерами 20, 10, 30, 40
ax.bar(categories, [20,10,30,40])
plt.show()