from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class EnabledChannelsMessage(NetworkMessage):
    protocolId = 9261
    channels:int
    disallowed:int
    
    
