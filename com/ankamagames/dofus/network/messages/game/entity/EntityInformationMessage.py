from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.entity.EntityInformation import EntityInformation


class EntityInformationMessage(NetworkMessage):
    protocolId = 7474
    entity:EntityInformation
    
