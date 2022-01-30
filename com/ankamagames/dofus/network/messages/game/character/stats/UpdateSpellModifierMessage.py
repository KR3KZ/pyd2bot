from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterSpellModification import CharacterSpellModification


class UpdateSpellModifierMessage(NetworkMessage):
    protocolId = 1672
    actorId:int
    spellModifier:CharacterSpellModification
    
