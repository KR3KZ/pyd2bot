from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class WrapperObjectDissociateRequestMessage(NetworkMessage):
    protocolId = 9634
    hostUID:int
    hostPos:int
    
