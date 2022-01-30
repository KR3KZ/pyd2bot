from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildPaddockRemovedMessage(INetworkMessage):
    protocolId = 9960
    paddockId:int
    
    
