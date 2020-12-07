class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        a.sort()
        self.maximumDifference = int(a[len(a)-1]) - int(a[0])

        if self.maximumDifference < 0:
            self.maximumDifference *= -1

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)