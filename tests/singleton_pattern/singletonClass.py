
from com.ankamagames.jerakine.metaclasses.singleton import Singleton


class A(metaclass=Singleton):
    def __init__(self, data=None) -> None:
        self.data = data
