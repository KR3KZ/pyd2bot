from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class JobCrafterDirectoryRemoveMessage(INetworkMessage):
    protocolId = 890
    jobId:int
    playerId:int
    
    
