from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristics import CharacterCharacteristics


class GameFightCharacteristics(NetworkMessage):
    characteristics:CharacterCharacteristics
    summoner:int
    summoned:bool
    invisibilityState:int
    
    
