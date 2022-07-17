import random

class TextGen:
    def __init__(self, alphabet:dict) -> None:
        _sum = 0
        for _v in alphabet.values():
            _sum += _v
        assert _sum == 1.0 # probability should sum up to exactly 1

        self.alphabet = alphabet

    def generate(self, text_length:int) -> str:
        out = ""
        for i in range(text_length):
            _c = 0
            _r = random.random()
            for _k,_v in self.alphabet.items():
                _c += _v
                if _r < _c:
                    out += _k
                    break
        return out