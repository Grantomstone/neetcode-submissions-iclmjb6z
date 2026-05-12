class CountSquares:

    def __init__(self):
        self.pointpos = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.pointpos[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        x, y = point
        output = 0
        for x_i, y_i in self.points:
            if (abs(x - x_i) != abs(y - y_i)) or x == x_i or y == y_i:
                continue
            output += self.pointpos[(x, y_i)] * self.pointpos[(x_i, y)]
        return output