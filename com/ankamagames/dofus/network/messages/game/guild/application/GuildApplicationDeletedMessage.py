from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildApplicationDeletedMessage(INetworkMessage):
    protocolId = 5546
    deleted:bool
    
    
