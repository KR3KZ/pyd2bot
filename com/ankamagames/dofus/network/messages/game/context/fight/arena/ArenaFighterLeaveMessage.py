from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterBasicMinimalInformations import CharacterBasicMinimalInformations


@dataclass
class ArenaFighterLeaveMessage(NetworkMessage):
    leaver:CharacterBasicMinimalInformations
    
    
    def __post_init__(self):
        super().__init__()
    