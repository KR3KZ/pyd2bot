from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ObjectEffect(INetworkMessage):
    protocolId = 5685
    actionId:int
    
    
