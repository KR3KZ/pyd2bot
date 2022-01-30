from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations


class TaxCollectorAttackedMessage(NetworkMessage):
    protocolId = 4728
    firstNameId:int
    lastNameId:int
    worldX:int
    worldY:int
    mapId:float
    subAreaId:int
    guild:BasicGuildInformations
    
