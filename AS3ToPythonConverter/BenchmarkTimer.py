class BenchmarkTimer(Timer):
    
    startedTimers:dict = dict(True)
    
    startWithoutResetCount:int = 0
    
    
    hasBeenReset:bool = True
    
    name:str = "unamed"
    
    def __init__(self, delay:int, repeatCount:int = 0, name:str = ""):
        self.name = name
        super().__init__(delay, repeatCount)
    
    def printUnstoppedTimers(self) -> None:
        timer = None
        unstoppedTimersCount:int = 0
        for timer in startedTimers:
            unstoppedTimersCount += 1
            LogInFile().logLine("This Timer is unstopped: " + timer.name, FileLoggerEnum.BENCHMARKTIMERS)
            LogInFile().logLine("Total unstopped Timers: " + unstoppedTimersCount, FileLoggerEnum.BENCHMARKTIMERS)
            LogInFile().logLine("Stop Recording BenchmarkTimers.", FileLoggerEnum.BENCHMARKTIMERS)
    
    def start(self) -> None:
        super().start()
        if not self.hasBeenReset:
        startWithoutResetCount += 1
        LogInFile().logLine("This Timer has not been reset before start: " + self.name, FileLoggerEnum.BENCHMARKTIMERS)
        if not startedTimers[self]:
        startedTimers[self] = True
        self.hasBeenReset = False
    
    def stop(self) -> None:
        super().stop()
        del startedTimers[self]
    
    def reset(self) -> None:
        super().reset()
        self.hasBeenReset = True
