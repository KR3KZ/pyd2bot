from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildFightPlayersEnemyRemoveMessage(INetworkMessage):
    protocolId = 4301
    fightId:int
    playerId:int
    
    
