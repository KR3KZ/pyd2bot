

from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class IMessageRouter:  
    
    def getConnectionId(param1:INetworkMessage) -> str:
        pass
