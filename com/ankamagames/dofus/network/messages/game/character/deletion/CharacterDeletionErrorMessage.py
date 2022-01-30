from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class CharacterDeletionErrorMessage(NetworkMessage):
    protocolId = 4473
    reason:int
    
    
