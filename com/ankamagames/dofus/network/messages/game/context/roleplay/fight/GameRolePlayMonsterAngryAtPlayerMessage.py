from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayMonsterAngryAtPlayerMessage(NetworkMessage):
    protocolId = 465
    playerId:int
    monsterGroupId:int
    angryStartTime:int
    attackTime:int
    
