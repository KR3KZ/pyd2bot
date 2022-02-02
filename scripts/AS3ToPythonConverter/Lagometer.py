from com.ankamagames.jerakine.benchmark.BenchmarkTimer import BenchmarkTimer
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.network.ILagometer import ILagometer
from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
class Lagometer(ILagometer):
   
   logger = Logger(__name__)
   
   SHOW_LAG_DELAY:int = 2 * 1000
   
   
   _timer:BenchmarkTimer
   
   _lagging:bool = False
   
   def __init__(self):
      super().__init__()
      self._timer = BenchmarkTimer(self.SHOW_LAG_DELAY,1,"Lagometer._timer")
      self._timer.addEventListener(TimerEvent.TIMER_COMPLETE,self.onTimerComplete)
   
   def ping(self, msg:INetworkMessage = None) -> None:
      self._timer.start()
      self._timer.addEventListener(TimerEvent.TIMER_COMPLETE,self.onTimerComplete)
   
   def pong(self, msg:INetworkMessage = None) -> None:
      if self._lagging:
         self.stopLag()
      self.stop()
   
   def stop(self) -> None:
      self._timer.stop()
      self._timer.removeEventListener(TimerEvent.TIMER_COMPLETE,self.onTimerComplete)
   
   def onTimerComplete(self, e:TimerEvent) -> None:
      self.stop()
      self.startLag()
   
   def startLag(self) -> None:
      if not self._lagging:
         UiStatsFrame.addStat("server_lag")
         UiStatsFrame.setDateStat("last_server_lag")
      self._lagging = True
      self.updateUi()
   
   def updateUi(self) -> None:
      KernelEventsManager().processCallback(HookList.LaggingNotification,self._lagging)
   
   def stopLag(self) -> None:
      self._lagging = False
      self.updateUi()
