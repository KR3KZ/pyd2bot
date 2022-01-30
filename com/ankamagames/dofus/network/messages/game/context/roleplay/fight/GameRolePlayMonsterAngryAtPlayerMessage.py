from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayMonsterAngryAtPlayerMessage(NetworkMessage):
    protocolId = 465
    playerId:float
    monsterGroupId:float
    angryStartTime:float
    attackTime:float
    
