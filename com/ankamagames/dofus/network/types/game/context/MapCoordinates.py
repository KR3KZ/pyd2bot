
from com.ankamagames.jerakine.network.customDataWrapper import ByteArray
from com.ankamagames.jerakine.network.INetworkType import INetworkType


class MapCoordinates(INetworkType):
      
      protocolId:int = 3568
       
      
      worldX:int = 0
      
      worldY:int = 0
      
      def __init__(self):
         super().__init__()
      
      def getTypeId(self) -> int:
         return 3568
      
      def initMapCoordinates(self, worldX:int = 0, worldY:int = 0) -> 'MapCoordinates':
         self.worldX = worldX
         self.worldY = worldY
         return self
      
      def reset(self) -> None:
         self.worldX = 0
         self.worldY = 0