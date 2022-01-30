from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameRolePlayAttackMonsterRequestMessage(INetworkMessage):
    protocolId = 3767
    monsterGroupId:int
    
    
