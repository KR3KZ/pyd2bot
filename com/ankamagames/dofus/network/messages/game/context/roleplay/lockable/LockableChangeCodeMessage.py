from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class LockableChangeCodeMessage(INetworkMessage):
    protocolId = 768
    code:str
    
    
