from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ReloginTokenStatusMessage(NetworkMessage):
    protocolId = 3172
    validToken:bool
    ticket:int
    
