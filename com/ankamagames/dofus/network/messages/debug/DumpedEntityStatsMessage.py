from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristics import CharacterCharacteristics


class DumpedEntityStatsMessage(NetworkMessage):
    protocolId = 3665
    actorId:float
    stats:CharacterCharacteristics
    
