from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class BreachRoomUnlockRequestMessage(INetworkMessage):
    protocolId = 8276
    roomId:int
    
    
