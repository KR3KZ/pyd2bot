from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class CharacterCreationResultMessage(NetworkMessage):
    protocolId = 110
    result:int
    
