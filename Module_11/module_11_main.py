from datetime import datetime
import requests
import pandas as pd
import numpy as np
column_text = []
data_text = []
dictionary = {}
with open ('data.txt', encoding= 'utf - 8') as file:
    for i in file.read().split():
        #Проверяет состоит ли текст только из чисел.
        if i.isdigit():
            data_text.append(list(i))
        else:
            column_text.append(i)


# Создаем таблицу с помощью pandas используя данные словаря. Ключ - название столбика, значение
df = pd.DataFrame(
    {"AAA":[4,5,6,7], "BBB":[40,50,60,70], "CCC":[400,500,600,700]}
)
# Меняем данные столбца BBB если в столбце ААА значение больше 5
df.loc[df.AAA > 5, "BBB" ] = 0

# добавляем колонку с именем logic и пишем в ней high если в ААА значение больше 5, иначе пишем low
df['logic'] = np.where(df["AAA"] > 5, 'high', 'low')
print(df)

# записывает в переменную даты в заданном формате, 6 месяцев как ЛИСТ.
dates = pd.date_range("20130101", periods=6)
print(dates)
print(column_text)
print(data_text)
d = dict(zip(column_text,data_text))
print(d)
df_2 = pd.DataFrame(d)
print(df_2)

# print(list(zip('abcdefg', range(5), range(5)))    )
      # df_mask = pd.DataFrame(
#     {"AAA": [True] * 4, "BBB": [False] * 4, "CCC": [False, True] * 2}
# )
# print(df.where(df_mask, -1000))
