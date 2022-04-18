from threading import Timer
from typing import Any


class SoftReference:
    def __init__(self, obj, keptTime: int = 10000):
        super().__init__()
        self.value = obj
        self.keptTime = keptTime
        self.resetTimeout()

    @property
    def object(self) -> Any:
        self.resetTimeout()
        return self.value

    def resetTimeout(self) -> None:
        self.timeout.cancel()
        if self.value:
            self.timeout = Timer(self.keptTime, self.clearReference)
            self.timeout.start()

    def clearReference(self) -> None:
        self.value = None
