from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterSpellModification import CharacterSpellModification


class UpdateSpellModifierMessage(NetworkMessage):
    actorId:int
    spellModifier:CharacterSpellModification
    
    
