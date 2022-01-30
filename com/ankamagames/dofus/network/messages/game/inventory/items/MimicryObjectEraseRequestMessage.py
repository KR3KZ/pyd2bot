from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MimicryObjectEraseRequestMessage(INetworkMessage):
    protocolId = 3575
    hostUID:int
    hostPos:int
    
    
