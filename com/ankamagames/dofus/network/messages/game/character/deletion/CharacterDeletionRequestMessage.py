from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class CharacterDeletionRequestMessage(INetworkMessage):
    protocolId = 8394
    characterId:int
    secretAnswerHash:str
    
    
