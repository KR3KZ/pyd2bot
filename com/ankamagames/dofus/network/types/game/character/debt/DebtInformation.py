from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class DebtInformation(NetworkMessage):
    protocolId = 9735
    id:float
    timestamp:float
    
