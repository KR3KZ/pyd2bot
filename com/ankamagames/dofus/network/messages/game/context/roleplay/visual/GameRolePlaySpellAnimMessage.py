from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GameRolePlaySpellAnimMessage(NetworkMessage):
    casterId:int
    targetCellId:int
    spellId:int
    spellLevel:int
    
    
    def __post_init__(self):
        super().__init__()
    