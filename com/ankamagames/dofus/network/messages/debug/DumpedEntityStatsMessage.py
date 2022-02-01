from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristics import CharacterCharacteristics


class DumpedEntityStatsMessage(NetworkMessage):
    actorId:int
    stats:CharacterCharacteristics
    
    
