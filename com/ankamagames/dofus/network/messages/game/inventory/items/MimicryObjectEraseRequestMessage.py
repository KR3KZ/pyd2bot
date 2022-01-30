from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MimicryObjectEraseRequestMessage(NetworkMessage):
    protocolId = 3575
    hostUID:int
    hostPos:int
    
