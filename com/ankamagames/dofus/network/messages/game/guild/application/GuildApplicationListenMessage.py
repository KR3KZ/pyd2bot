from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildApplicationListenMessage(INetworkMessage):
    protocolId = 9375
    listen:bool
    
    
