from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class EnabledChannelsMessage(INetworkMessage):
    protocolId = 9261
    channels:int
    disallowed:int
    
    
