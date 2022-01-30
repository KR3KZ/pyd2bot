from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ServerOptionalFeaturesMessage(NetworkMessage):
    protocolId = 189
    features:int
    
    
