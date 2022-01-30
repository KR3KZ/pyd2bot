from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameRolePlayMonsterAngryAtPlayerMessage(INetworkMessage):
    protocolId = 465
    playerId:int
    monsterGroupId:int
    angryStartTime:int
    attackTime:int
    
    
