from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayMonsterAngryAtPlayerMessage(NetworkMessage):
    playerId:int
    monsterGroupId:int
    angryStartTime:int
    attackTime:int
    
    
