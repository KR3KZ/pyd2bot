from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations
    


class TaxCollectorAttackedMessage(NetworkMessage):
    firstNameId:int
    lastNameId:int
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    guild:'BasicGuildInformations'
    

    def init(self, firstNameId:int, lastNameId:int, worldX:int, worldY:int, mapId:int, subAreaId:int, guild:'BasicGuildInformations'):
        self.firstNameId = firstNameId
        self.lastNameId = lastNameId
        self.worldX = worldX
        self.worldY = worldY
        self.mapId = mapId
        self.subAreaId = subAreaId
        self.guild = guild
        
        super().__init__()
    
    