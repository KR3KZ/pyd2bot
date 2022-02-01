from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameRolePlayMonsterAngryAtPlayerMessage(INetworkMessage):
    protocolId = 465
    playerId:int
    monsterGroupId:int
    angryStartTime:int
    attackTime:int
    
    
