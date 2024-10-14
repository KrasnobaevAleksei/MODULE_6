def custom_write(file_name, strings: list):
    open_file = open(file_name, "w", encoding= "utf - 8")
    string_position = {}
    n = 0
    for i in strings:
        n+=1
        pos = open_file.tell()
        open_file.write(i + "\n")
        string_position[n, str(pos)] = i
    open_file.close()
    return string_position

if __name__ == "__main__":
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
