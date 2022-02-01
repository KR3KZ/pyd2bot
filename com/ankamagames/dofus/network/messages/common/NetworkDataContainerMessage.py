from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray
from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class NetworkDataContainerMessage(INetworkMessage):
    protocolId = 2
    content:ByteArray
    
    
