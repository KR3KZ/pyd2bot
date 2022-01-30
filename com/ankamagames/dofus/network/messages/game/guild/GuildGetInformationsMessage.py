from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildGetInformationsMessage(INetworkMessage):
    protocolId = 5805
    infoType:int
    
    
