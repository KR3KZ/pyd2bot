from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildFightPlayersEnemyRemoveMessage(NetworkMessage):
    fightId:int
    playerId:int
    
    
