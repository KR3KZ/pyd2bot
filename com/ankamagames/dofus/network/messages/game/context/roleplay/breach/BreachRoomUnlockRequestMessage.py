from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class BreachRoomUnlockRequestMessage(NetworkMessage):
    protocolId = 8276
    roomId:int
    
