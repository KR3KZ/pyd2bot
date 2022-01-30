from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.quest.GameRolePlayNpcQuestFlag import GameRolePlayNpcQuestFlag


class MapNpcQuestInfo(NetworkMessage):
    protocolId = 7429
    mapId:float
    npcsIdsWithQuest:list[int]
    questFlags:list[GameRolePlayNpcQuestFlag]
    
