class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

class SafeFourCal(MoreFourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = FourCal(4, 2)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

b = MoreFourCal(4,2)
print(b.pow())
print(b.add())
print(b.sub())
print(b.mul())
print(b.div())

c = SafeFourCal(3,0)
print(c.div())