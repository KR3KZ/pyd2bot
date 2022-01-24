class IF:

    s = 0


class F1(IF):

    @staticmethod
    def process():
        F1.s = 1


class F2(IF):

    @staticmethod
    def process():
        F2.s = 1


i1 = F1()
i2 = F1()

print(i1.s)
print(i2.s)
i1.process()
print(i1.s)
print(i2.s)