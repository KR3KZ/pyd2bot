from com.ankamagames.jerakine.metaclasses.singleton import Singleton


class TimeManager(metaclass=Singleton):

    def __init__(self) -> None:
        self.serverTimeLag:int = 0
        
        self.serverUtcTimeLag:int = 0

        self.timezoneOffset:int = 0
        
        self.dofusTimeYearLag:int = 0