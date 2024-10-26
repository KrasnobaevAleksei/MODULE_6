def apply_all_function(int_list, *function):
    dict_all={}
    int_list = list(filter(int_or_float, int_list))
    for numbers in function:
        dict_all[numbers.__name__] = numbers(int_list)
    return dict_all

def int_or_float(x):
    return isinstance(x, (int, float))

print(apply_all_function([6, 20, 15, 9], max, min))
print(apply_all_function([6, 20, 15, 9], len, sum, sorted))