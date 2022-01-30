from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.entity.EntityInformation import EntityInformation


class EntitiesInformationMessage(NetworkMessage):
    protocolId = 5147
    entities:EntityInformation
    
    
