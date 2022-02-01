from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class BreachRoomUnlockRequestMessage(INetworkMessage):
    protocolId = 8276
    roomId:int
    
    
