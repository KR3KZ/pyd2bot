from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildFightPlayersEnemyRemoveMessage(INetworkMessage):
    protocolId = 4301
    fightId:int
    playerId:int
    
    
