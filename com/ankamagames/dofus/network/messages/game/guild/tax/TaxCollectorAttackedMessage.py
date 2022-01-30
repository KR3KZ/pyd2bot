from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations


class TaxCollectorAttackedMessage(INetworkMessage):
    protocolId = 4728
    firstNameId:int
    lastNameId:int
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    guild:BasicGuildInformations
    
    
