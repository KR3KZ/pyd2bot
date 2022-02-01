from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CharacterDeletionRequestMessage(NetworkMessage):
    characterId:int
    secretAnswerHash:str
    
    
