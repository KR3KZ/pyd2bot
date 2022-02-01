from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class CharacterDeletionErrorMessage(INetworkMessage):
    protocolId = 4473
    reason:int
    
    
