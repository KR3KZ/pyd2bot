from com.ankamagames.jerakine.network.iNetworkType import INetworkType


class AbstractCharacterInformation(INetworkType):

   id:float = 0
   
   def __init__(self):
      super().__init__()
   
   def initAbstractCharacterInformation(self, id:float = 0) -> 'AbstractCharacterInformation':
      self.id = id
      return self
   
   def reset(self) -> None:
      self.id = 0