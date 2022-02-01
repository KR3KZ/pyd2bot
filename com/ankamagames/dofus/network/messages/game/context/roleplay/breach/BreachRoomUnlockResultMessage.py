from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class BreachRoomUnlockResultMessage(INetworkMessage):
    protocolId = 3212
    roomId:int
    result:int
    
    
