from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterSpellModification import CharacterSpellModification
    


class UpdateSpellModifierMessage(NetworkMessage):
    actorId:int
    spellModifier:'CharacterSpellModification'
    

    def init(self, actorId:int, spellModifier:'CharacterSpellModification'):
        self.actorId = actorId
        self.spellModifier = spellModifier
        
        super().__init__()
    
    