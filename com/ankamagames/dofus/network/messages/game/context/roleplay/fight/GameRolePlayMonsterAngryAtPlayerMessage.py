from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GameRolePlayMonsterAngryAtPlayerMessage(NetworkMessage):
    playerId:int
    monsterGroupId:int
    angryStartTime:int
    attackTime:int
    
    
    def __post_init__(self):
        super().__init__()
    