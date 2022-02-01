from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ServerOptionalFeaturesMessage(INetworkMessage):
    protocolId = 189
    features:int
    
    
