class Atbash:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self):
        lowercase_code = {x: y for x, y in zip(self.alphabet, self.alphabet[::-1])}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, self.alphabet[::-1])}
        self._encode = lowercase_code
        self._encode.update(uppercase_code)

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])


cipher = Atbash()
line = input()
while line != '.':
    print(cipher.encode(line))
    line = input()

class Deshifrator:
    alphabet1 = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"
    def __init__(self):
        lowercase_code = {x: y for x, y in zip(self.alphabet1, self.alphabet1[::-1])}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet1, self.alphabet1[::-1])}
        self._encode = lowercase_code
        self._encode.update(uppercase_code)

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])


cipher = Deshifrator()
line = input()
while line != '.':
    print(cipher.encode(line))
    line = input()