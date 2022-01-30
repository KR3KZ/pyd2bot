from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class JobBookSubscribeRequestMessage(INetworkMessage):
    protocolId = 4809
    jobIds:int
    
    
