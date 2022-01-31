from threading import Timer
from com.ankamagames.jerakine.benchmark.FileLoggerEnum import FileLoggerEnum
from com.ankamagames.jerakine.logger.Logger import Logger


class BenchmarkTimer(Timer):
    
    startedTimers = set['BenchmarkTimer']()
    
    startWithoutResetCount:int = 0

    hasBeenReset:bool = True
    
    name:str = "unamed"
    
    logger = Logger(FileLoggerEnum.BENCHMARKTIMERS)
    
    def __init__(self, delay:int, repeatCount:int = 0, name:str = ""):
        super().__init__(delay, repeatCount, name)
        
    def printUnstoppedTimers(self) -> None:
        unstoppedTimersCount:int = 0
        for timer in BenchmarkTimer.startedTimers:
            unstoppedTimersCount += 1
            self.logger.info("This Timer is unstopped: ")
            self.logger.info("Total unstopped Timers: " + str(unstoppedTimersCount))
            self.logger.info("Stop Recording BenchmarkTimers.")
    
    def start(self) -> None:
        super().start()
        if not self.hasBeenReset:
            self.startWithoutResetCount += 1
            self.logger.info("This Timer has not been reset before start: " + self.name)
        if not BenchmarkTimer.startedTimers.get(self):
            BenchmarkTimer.startedTimers.add(self)
        self.hasBeenReset = False
    
    def stop(self) -> None:
        super().stop()
        del BenchmarkTimer.startedTimers[self]
    
    def reset(self) -> None:
        super().reset()
        self.hasBeenReset = True
