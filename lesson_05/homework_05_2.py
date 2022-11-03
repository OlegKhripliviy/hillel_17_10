class Frange:
    def __init__(self, start, stop=None, step=None):
        self.start = start
        self.stop = stop
        self.step = step if step else 1

        if self.stop is None:
            self.stop = 0
            self.start, self.stop = self.stop, self.start

        if self.stop < self.start and self.step < 0:
            self.count = self.start - self.step

        elif self.stop > self.start and self.step > 0:
            self.count = self.start - self.step

    def __iter__(self):
        return self

    def __next__(self):

        if self.stop < self.start and self.step < 0:
            self.count += self.step
            if self.count <= self.stop:
                raise StopIteration("stop")
            else:
                return self.count

        elif self.stop > self.start and self.step > 0:
            self.count += self.step
            if self.count >= self.stop:
                raise StopIteration("stop")
            else:
                return round(self.count, 1)
        else:
            raise StopIteration("stop")


assert list(Frange(5)) == [0, 1, 2, 3, 4]
assert list(Frange(2, 5)) == [2, 3, 4]
assert list(Frange(2, 10, 2)) == [2, 4, 6, 8]
assert list(Frange(10, 2, -2)) == [10, 8, 6, 4]
assert list(Frange(2, 5.5, 1.5)) == [2, 3.5, 5]
assert list(Frange(1, 5)) == [1, 2, 3, 4]
assert list(Frange(0, 5)) == [0, 1, 2, 3, 4]
assert list(Frange(0, 0)) == []
assert list(Frange(100, 0)) == []
assert list(Frange(-5)) == []


print("SUCCESS!")
