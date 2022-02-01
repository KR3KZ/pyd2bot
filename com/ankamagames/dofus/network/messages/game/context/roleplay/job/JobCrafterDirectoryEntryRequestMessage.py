from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class JobCrafterDirectoryEntryRequestMessage(INetworkMessage):
    protocolId = 3858
    playerId:int
    
    
