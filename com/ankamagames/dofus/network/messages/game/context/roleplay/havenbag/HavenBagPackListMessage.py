from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class HavenBagPackListMessage(INetworkMessage):
    protocolId = 268
    packIds:int
    
    
