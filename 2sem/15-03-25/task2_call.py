from random import randint, choice

class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        length = randint(self.min_length, self.max_length)
        password = ''.join(choice(self.psw_chars) for i in range(length))
        return password
rnd = RandomPassword("qwerttywproeituweroptiwr", 5, 20)
psw = rnd()
print(psw)
