from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class BreachRoomUnlockResultMessage(NetworkMessage):
    protocolId = 3212
    roomId:int
    result:int
    
    
