class Obj:

    _a: int = 1

    @property
    def a(self) -> int:
        return self._a

    @a.setter
    def a(self, value: int) -> None:
        self._a = value

    def copy(self, x: "Obj", y: "Obj") -> None:
        x.a = y.a


x = Obj()
y = Obj()
y.a = 10

x.copy(x, y)
print(x.a)
