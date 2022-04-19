
from com.ankamagames.jerakine.metaclasses.Singleton import Singleton


class A(metaclass=Singleton):
    def __init__(self, data=None) -> None:
        self.data = data
