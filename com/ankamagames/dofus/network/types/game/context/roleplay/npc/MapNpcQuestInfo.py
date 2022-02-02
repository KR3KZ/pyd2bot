from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.quest.GameRolePlayNpcQuestFlag import GameRolePlayNpcQuestFlag


@dataclass
class MapNpcQuestInfo(NetworkMessage):
    mapId:int
    npcsIdsWithQuest:list[int]
    questFlags:list[GameRolePlayNpcQuestFlag]
    
    
    def __post_init__(self):
        super().__init__()
    