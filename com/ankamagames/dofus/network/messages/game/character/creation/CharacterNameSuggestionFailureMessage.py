from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class CharacterNameSuggestionFailureMessage(NetworkMessage):
    protocolId = 3074
    reason:int
    
    
