from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildFightPlayersHelpersLeaveMessage(INetworkMessage):
    protocolId = 5749
    fightId:int
    playerId:int
    
    
