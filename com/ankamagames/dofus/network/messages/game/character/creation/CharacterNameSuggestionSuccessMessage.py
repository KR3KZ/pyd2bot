from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class CharacterNameSuggestionSuccessMessage(NetworkMessage):
    protocolId = 428
    suggestion:str
    
