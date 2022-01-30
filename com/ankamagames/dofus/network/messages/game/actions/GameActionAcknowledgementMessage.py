from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameActionAcknowledgementMessage(NetworkMessage):
    protocolId = 3561
    valid:bool
    actionId:int
    
    
