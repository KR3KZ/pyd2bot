from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.quest.GameRolePlayNpcQuestFlag import GameRolePlayNpcQuestFlag
    


class MapNpcQuestInfo(NetworkMessage):
    mapId:int
    npcsIdsWithQuest:list[int]
    questFlags:list['GameRolePlayNpcQuestFlag']
    

    def init(self, mapId:int, npcsIdsWithQuest:list[int], questFlags:list['GameRolePlayNpcQuestFlag']):
        self.mapId = mapId
        self.npcsIdsWithQuest = npcsIdsWithQuest
        self.questFlags = questFlags
        
        super().__init__()
    
    