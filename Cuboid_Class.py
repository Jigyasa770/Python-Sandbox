class Cuboid:
    count = 0
    def __init__(self, l, b, h):
        self.length = l
        self.breadth = b
        self.height = h
        Cuboid.count += 1

    def lidarea(self):
        return self.length * self.breadth

    def tsa(self):
        return 2 * ((self.length * self.breadth) + (self.length * self.height) + (self.breadth * self.height))

    def vol(self):
        return self.length * self.breadth * self.height
    @classmethod
    def cuboidcount(cls):
       print(cls.count)

c1 = Cuboid(10, 5, 3)
print(c1.vol())
c2 = Cuboid(20, 10, 30)
print(c2.tsa())
c3 = Cuboid(15, 27, 99)
print(c3.lidarea())
Cuboid.cuboidcount()