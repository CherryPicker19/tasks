class WordString:
    def __init__(self, string=''):
        self.string = string

    def __len__(self):
        return len(self.string.split(' '))

    def __call__(self, idx):
        return self.string.split(' ')[idx]

words = WordString()
words.string = "Python ООП"
n = len(words)
print(words.string)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")