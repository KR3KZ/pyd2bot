from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.entity.EntityInformation import EntityInformation


class EntitiesInformationMessage(NetworkMessage):
    entities:list[EntityInformation]
    
    
