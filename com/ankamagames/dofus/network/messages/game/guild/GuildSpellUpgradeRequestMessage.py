from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GuildSpellUpgradeRequestMessage(NetworkMessage):
    spellId:int
    
    
    def __post_init__(self):
        super().__init__()
    