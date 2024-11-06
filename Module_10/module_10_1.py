import threading
import time

def write_words(words_count : int, file_name):
    with open(file_name, "w", encoding= "utf-8") as file:
        for i in range(words_count):
            file.write(f"Какое-то слово № {i} \n" )
            time.sleep(0.1)
        print(f"Завершилась запись в файл {file_name}")
start = time.time()
write_words(10,"example1.txt")
write_words(30,"example2.txt")
write_words(200,"example3.txt")
write_words(100,"example4.txt")
finish = time.time()
print(f"Работа потоков {finish - start}")

thread = threading.Thread(target=write_words, args=(10,"example5.txt" ))
thread2 = threading.Thread(target=write_words, args=(30,"example6.txt" ))
thread3 = threading.Thread(target=write_words, args=(200,"example7.txt" ))
thread4 = threading.Thread(target=write_words, args=(100,"example8.txt" ))

start2 = time.time()

thread.start()
thread2.start()
thread3.start()
thread4.start()
thread.join()
thread2.join()
thread3.join()
thread4.join()

finish2 = time.time()
print(f"Работа потоков {finish2 - start2} ")

