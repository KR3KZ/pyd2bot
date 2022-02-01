from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class CharacterNameSuggestionSuccessMessage(INetworkMessage):
    protocolId = 428
    suggestion:str
    
    
