from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MountInformationRequestMessage(INetworkMessage):
    protocolId = 2112
    id:int
    time:int
    
    
