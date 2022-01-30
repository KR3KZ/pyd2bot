from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class CharacterNameSuggestionSuccessMessage(INetworkMessage):
    protocolId = 428
    suggestion:str
    
    
