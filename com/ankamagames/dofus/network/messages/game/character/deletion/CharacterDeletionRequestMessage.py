from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class CharacterDeletionRequestMessage(INetworkMessage):
    protocolId = 8394
    characterId:int
    secretAnswerHash:str
    
    
