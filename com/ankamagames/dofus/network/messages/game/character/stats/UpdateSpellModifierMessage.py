from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterSpellModification import CharacterSpellModification


@dataclass
class UpdateSpellModifierMessage(NetworkMessage):
    actorId:int
    spellModifier:CharacterSpellModification
    
    
    def __post_init__(self):
        super().__init__()
    