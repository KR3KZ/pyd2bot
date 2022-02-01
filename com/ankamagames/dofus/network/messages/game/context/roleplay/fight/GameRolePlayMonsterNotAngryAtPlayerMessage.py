from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameRolePlayMonsterNotAngryAtPlayerMessage(INetworkMessage):
    protocolId = 7726
    playerId:int
    monsterGroupId:int
    
    
