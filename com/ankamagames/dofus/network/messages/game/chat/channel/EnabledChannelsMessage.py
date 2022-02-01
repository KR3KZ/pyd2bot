from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class EnabledChannelsMessage(NetworkMessage):
    channels:list[int]
    disallowed:list[int]
    
    
