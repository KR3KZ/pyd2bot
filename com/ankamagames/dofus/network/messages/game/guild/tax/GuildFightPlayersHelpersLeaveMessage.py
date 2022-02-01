from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildFightPlayersHelpersLeaveMessage(INetworkMessage):
    protocolId = 5749
    fightId:int
    playerId:int
    
    
