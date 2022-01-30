from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.entity.EntityInformation import EntityInformation


class EntitiesInformationMessage(INetworkMessage):
    protocolId = 5147
    entities:EntityInformation
    
    
