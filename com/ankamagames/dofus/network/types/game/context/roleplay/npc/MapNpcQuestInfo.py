from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.quest.GameRolePlayNpcQuestFlag import GameRolePlayNpcQuestFlag


class MapNpcQuestInfo(INetworkMessage):
    protocolId = 7429
    mapId:int
    npcsIdsWithQuest:int
    questFlags:GameRolePlayNpcQuestFlag
    
    
