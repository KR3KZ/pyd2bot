from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayAttackMonsterRequestMessage(NetworkMessage):
    protocolId = 3767
    monsterGroupId:int
    
    
