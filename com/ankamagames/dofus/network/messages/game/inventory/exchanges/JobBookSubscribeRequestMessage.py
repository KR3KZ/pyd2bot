from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class JobBookSubscribeRequestMessage(INetworkMessage):
    protocolId = 4809
    jobIds:int
    
    
