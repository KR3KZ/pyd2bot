from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildKickRequestMessage(INetworkMessage):
    protocolId = 3965
    kickedId:int
    
    
