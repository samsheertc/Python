class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]


def sentence(sentence):
    for word in sentence.split():
        yield word
		

#Class for Iterator
my_sentance = Sentance("This is a test")

#Genrator
my_sentance = sentance("This is a test")


for word in my_sentance:
    print(word)

print(next(my_sentance))
print(next(my_sentance))
print(next(my_sentance))
print(next(my_sentance))
print(next(my_sentance))
