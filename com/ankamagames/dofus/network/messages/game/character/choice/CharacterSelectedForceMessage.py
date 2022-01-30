from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class CharacterSelectedForceMessage(NetworkMessage):
    protocolId = 6158
    id:int
    
    
