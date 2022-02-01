from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ObjectGroundRemovedMultipleMessage(INetworkMessage):
    protocolId = 6993
    cells:int
    
    
