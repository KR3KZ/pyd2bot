from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.quest.GameRolePlayNpcQuestFlag import GameRolePlayNpcQuestFlag


class MapNpcQuestInfo(NetworkMessage):
    mapId:int
    npcsIdsWithQuest:list[int]
    questFlags:list[GameRolePlayNpcQuestFlag]
    
    
