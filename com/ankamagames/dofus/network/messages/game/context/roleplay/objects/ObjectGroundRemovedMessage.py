from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ObjectGroundRemovedMessage(INetworkMessage):
    protocolId = 7554
    cell:int
    
    
