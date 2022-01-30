from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameRolePlayMonsterNotAngryAtPlayerMessage(INetworkMessage):
    protocolId = 7726
    playerId:int
    monsterGroupId:int
    
    
