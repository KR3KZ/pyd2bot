from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class CharacterDeletionRequestMessage(NetworkMessage):
    protocolId = 8394
    characterId:int
    secretAnswerHash:str
    
    
