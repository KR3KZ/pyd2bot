from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicDetailed import CharacterCharacteristicDetailed


class CharacterSpellModification(NetworkMessage):
    protocolId = 4425
    modificationType:int
    spellId:int
    value:CharacterCharacteristicDetailed
    
    
