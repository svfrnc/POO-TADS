import random

class bingo:
    def __init__(self, bolas, numBolas):
        self.__numBolas = __numBolas
        self.__bolas = []
    def proximo(self):
        if len(self.__bolas) == self.__numBolas:
            return -1
            x =random.randint(1, self.__numBolas)
            while x in self.__bolas:
                x = random.randint(1, self.__numBolas)
                self.__bolas.append(x)
                return x
        def sorteados(self):
            return self.__bolas
    b = bingo(10)
