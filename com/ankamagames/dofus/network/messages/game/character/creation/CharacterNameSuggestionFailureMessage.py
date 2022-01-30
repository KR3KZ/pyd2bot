from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class CharacterNameSuggestionFailureMessage(INetworkMessage):
    protocolId = 3074
    reason:int
    
    
