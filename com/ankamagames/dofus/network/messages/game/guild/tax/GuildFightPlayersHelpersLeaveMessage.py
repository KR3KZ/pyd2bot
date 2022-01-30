from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildFightPlayersHelpersLeaveMessage(NetworkMessage):
    protocolId = 5749
    fightId:float
    playerId:float
    
