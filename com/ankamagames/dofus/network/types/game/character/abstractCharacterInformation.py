from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AbstractCharacterInformation(NetworkMessage):
    protocolId = 2714
    id:int
    
    
