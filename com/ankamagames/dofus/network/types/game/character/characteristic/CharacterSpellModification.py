from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicDetailed import CharacterCharacteristicDetailed


class CharacterSpellModification(NetworkMessage):
    modificationType:int
    spellId:int
    value:CharacterCharacteristicDetailed
    
    
