from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicDetailed import CharacterCharacteristicDetailed


class CharacterSpellModification(INetworkMessage):
    protocolId = 4425
    modificationType:int
    spellId:int
    value:CharacterCharacteristicDetailed
    
    
