import string
class WordsFinder:
    file_names = []
    def __init__(self, *files):
        for file in files:
            self.file_names.append(file)

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, encoding= "utf - 8") as file:
                    text  = file.read()
                    # удаляем знаки припинания из текста
                    table = str.maketrans(" ", " ", string.punctuation)
                    text2 = text.translate(table)
                    # словарь
                    all_words[name] = text2.split()
        return all_words

    def find(self, find_word : str):
        result = {}
        n = 0
        for name, words in self.get_all_words().items():
           for i in words:
               n += 1
               if i.lower() == find_word.lower():
                   result[name] = n
                   break
        return result

    def count(self, find_word : str):
        result = {}
        n = 0
        for name, words in self.get_all_words().items():
            # list_.append(name)
           for i in words:
               if i.lower() == find_word.lower():
                   n += 1
           result[name] = n
        return result

if __name__ == "__main__":
    # finder2 = WordsFinder('test_file.txt')
    # print(finder2.get_all_words())  # Все слова
    # print(finder2.find('TEXT'))  # 3 слово по счёту
    # print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

    # finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
    # print(finder1.get_all_words())
    # print(finder1.find('captain'))
    # print(finder1.count('captain'))

    finder1 = WordsFinder('Mother Goose - Monday’s Child.txt', )
    print(finder1.get_all_words())
    print(finder1.find('Child'))
    print(finder1.count('Child'))



