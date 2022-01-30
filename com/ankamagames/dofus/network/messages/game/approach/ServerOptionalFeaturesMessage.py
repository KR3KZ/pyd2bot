from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ServerOptionalFeaturesMessage(INetworkMessage):
    protocolId = 189
    features:int
    
    
