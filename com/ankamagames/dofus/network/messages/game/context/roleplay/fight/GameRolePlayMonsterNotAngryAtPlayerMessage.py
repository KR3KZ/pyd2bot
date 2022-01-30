from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayMonsterNotAngryAtPlayerMessage(NetworkMessage):
    protocolId = 7726
    playerId:int
    monsterGroupId:int
    
