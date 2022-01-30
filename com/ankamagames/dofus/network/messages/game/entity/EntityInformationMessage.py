from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.entity.EntityInformation import EntityInformation


class EntityInformationMessage(INetworkMessage):
    protocolId = 7474
    entity:EntityInformation
    
    
