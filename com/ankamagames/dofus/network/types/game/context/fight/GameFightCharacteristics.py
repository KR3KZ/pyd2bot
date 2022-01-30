from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristics import CharacterCharacteristics


class GameFightCharacteristics(NetworkMessage):
    protocolId = 7425
    characteristics:CharacterCharacteristics
    summoner:int
    summoned:bool
    invisibilityState:int
    
    
