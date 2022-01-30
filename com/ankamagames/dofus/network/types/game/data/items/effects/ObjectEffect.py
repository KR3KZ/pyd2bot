from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ObjectEffect(INetworkMessage):
    protocolId = 5685
    actionId:int
    
    
