def personal_sum(numbers):
    result_ = 0
    incorrect_data = 0
    for i  in numbers:
        try:
            result_ += i
        except TypeError as exc:
            incorrect_data +=1
    return (result_, incorrect_data)

def calculate_average(numbers : list):
    result_ = 0
    try:
        sum_num = personal_sum(numbers)[0]
        length_num = len(numbers) - personal_sum(numbers)[1]

        result_ = sum_num/length_num
    except TypeError as exc:
        print(f'В numbers записан некорректный тип данных')
        return None
    except ZeroDivisionError as exc:
        return 0
    return result_

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

# print(personal_sum([1, "Строка", 3, "Ещё Строка"]))
# print(type(personal_sum([1, "Строка", 3, "Ещё Строка"])))

