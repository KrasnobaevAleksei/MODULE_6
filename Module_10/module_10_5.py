import time
from multiprocessing import Pool

def  read_info(name):
    all_data = []
    with open(name, encoding="utf - 8") as file:
        for i in file:
            all_data.append(i)
filenames = [f'./file {number}.txt' for number in range(1, 5)]

# start = time.time()
# read_info(filenames[0])
# read_info(filenames[1])
# read_info(filenames[2])
# read_info(filenames[3])
# finish = time.time()
# print(f"{finish - start}(линейный)")

if __name__ == "__main__":
    start = time.time()
    with Pool(4) as pool:
        pool.map(read_info,filenames)
    finish = time.time()
    print(f"{finish - start}(многопроцессный)")