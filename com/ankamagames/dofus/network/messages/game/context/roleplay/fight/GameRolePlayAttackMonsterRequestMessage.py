from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameRolePlayAttackMonsterRequestMessage(INetworkMessage):
    protocolId = 3767
    monsterGroupId:int
    
    
