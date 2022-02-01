from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ServerOptionalFeaturesMessage(NetworkMessage):
    features:list[int]
    
    
