from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class JobBookSubscribeRequestMessage(NetworkMessage):
    protocolId = 4809
    jobIds:int
    
    
