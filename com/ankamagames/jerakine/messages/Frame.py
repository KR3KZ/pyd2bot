from com.ankamagames.jerakine.messages.messageHandler import MessageHandler
from com.ankamagames.jerakine.utils.misc.priotizable import Prioritizable


class Frame(MessageHandler, Prioritizable):
      
   
   def appended() -> bool:
      pass
   
   def pulled(self) -> bool:
      pass
