from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class CharacterDeletionErrorMessage(INetworkMessage):
    protocolId = 4473
    reason:int
    
    
