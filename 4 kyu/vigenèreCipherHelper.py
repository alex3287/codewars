class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.alphabet = alphabet
        self.matrix_abc = self.create_matrix(alphabet)
        self.key = key

    def create_matrix(self, alphabet):
        n = len(alphabet)
        matrix = []
        for i in range(n):
            abc = list(alphabet[i:] + alphabet[:i])
            matrix.append(abc)
        return matrix

    def create_new_key(self, key, text):
        if len(text) <= len(key):
            new_key = key[:len(text)]
        else:
            n = len(text) // len(key)
            n2 = len(text) % len(key)
            new_key = key * n + key[:n2]
        return new_key


    def encode(self, text):
        new_key = self.create_new_key(self.key, text)
        result = ''
        for i in range(len(text)):
            if text[i] in self.alphabet:
                result += self.matrix_abc[self.alphabet.index(new_key[i])][self.alphabet.index(text[i])]
            else:
                result += text[i]
        return result

    def decode(self, text):
        new_key = self.create_new_key(self.key, text)
        result = ''
        for i in range(len(text)):
            if text[i] in self.alphabet:
                row = self.alphabet.index(new_key[i])
                letter = self.matrix_abc[row].index(text[i])
                result += self.alphabet[letter]
            else:
                result += text[i]
        return result


abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"
test = VigenereCipher(key, abc)
# print(test.alphabet)
# print(test.matrix_abc)
# print(test.create_new_key(key, 'Hellowor'))
print(test.encode('codewars'))
print(test.decode('rovwsoiv'))