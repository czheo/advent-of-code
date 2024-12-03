import sys

s = sys.stdin.read()

class ParseException(Exception):
    pass

class Parser:
    def __init__(self, s):
        self.src = s
        self.idx = 0

    def parse(self):
        ret = 0
        while self.idx < len(self.src):
            ret += self.parseMul()
        return ret

    def parseMul(self):
        def char(c):
            if self.idx < len(self.src) and self.src[self.idx] == c:
                self.idx += 1
            else:
                raise ParseException

        def num():
            s = self.idx
            while self.idx < len(self.src) and self.src[self.idx].isdigit():
                self.idx += 1
            if s == self.idx:
                raise ParseException
            return int(self.src[s:self.idx])

        if self.src[self.idx: self.idx + 3] == 'mul':
            self.idx += 3
            try:
                char('(')
                x = num()
                char(',')
                y = num()
                char(')')
                return x * y
            except ParseException:
                return 0
        else:
            self.idx += 1
            return 0

p = Parser(s)
print(p.parse())

