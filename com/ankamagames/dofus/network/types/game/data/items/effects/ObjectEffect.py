from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ObjectEffect(NetworkMessage):
    protocolId = 5685
    actionId:int
    
    
