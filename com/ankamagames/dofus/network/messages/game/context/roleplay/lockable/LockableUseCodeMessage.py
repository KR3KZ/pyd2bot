from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class LockableUseCodeMessage(INetworkMessage):
    protocolId = 5618
    code:str
    
    
