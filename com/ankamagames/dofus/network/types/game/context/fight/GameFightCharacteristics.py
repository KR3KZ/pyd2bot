from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristics import CharacterCharacteristics


class GameFightCharacteristics(INetworkMessage):
    protocolId = 7425
    characteristics:CharacterCharacteristics
    summoner:int
    summoned:bool
    invisibilityState:int
    
    
