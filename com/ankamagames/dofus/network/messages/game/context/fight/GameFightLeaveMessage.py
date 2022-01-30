from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightLeaveMessage(NetworkMessage):
    protocolId = 4663
    charId:int
    
    
