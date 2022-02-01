from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class EnabledChannelsMessage(INetworkMessage):
    protocolId = 9261
    channels:int
    disallowed:int
    
    
