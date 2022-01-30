from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class CharacterLevelUpMessage(NetworkMessage):
    protocolId = 6501
    newLevel:int
    
    
