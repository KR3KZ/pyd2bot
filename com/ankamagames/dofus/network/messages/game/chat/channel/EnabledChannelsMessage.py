from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class EnabledChannelsMessage(NetworkMessage):
    protocolId = 9261
    channels:list[int]
    disallowed:list[int]
    
