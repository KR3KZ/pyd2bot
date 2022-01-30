from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class DebtInformation(NetworkMessage):
    protocolId = 9735
    id:int
    timestamp:int
    
