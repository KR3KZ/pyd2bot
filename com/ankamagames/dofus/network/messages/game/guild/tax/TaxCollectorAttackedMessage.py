from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations


class TaxCollectorAttackedMessage(NetworkMessage):
    firstNameId:int
    lastNameId:int
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    guild:BasicGuildInformations
    
    
