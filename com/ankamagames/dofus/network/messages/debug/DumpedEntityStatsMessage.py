from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristics import CharacterCharacteristics


class DumpedEntityStatsMessage(INetworkMessage):
    protocolId = 3665
    actorId:int
    stats:CharacterCharacteristics
    
    
