from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class CharacterNameSuggestionFailureMessage(INetworkMessage):
    protocolId = 3074
    reason:int
    
    
