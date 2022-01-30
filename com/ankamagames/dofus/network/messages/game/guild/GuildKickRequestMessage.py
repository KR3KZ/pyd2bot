from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildKickRequestMessage(NetworkMessage):
    protocolId = 3965
    kickedId:float
    
