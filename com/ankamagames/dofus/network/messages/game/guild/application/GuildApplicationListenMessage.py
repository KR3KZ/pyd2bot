from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildApplicationListenMessage(INetworkMessage):
    protocolId = 9375
    listen:bool
    
    
