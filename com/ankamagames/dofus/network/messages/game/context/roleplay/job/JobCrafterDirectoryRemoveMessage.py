from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class JobCrafterDirectoryRemoveMessage(INetworkMessage):
    protocolId = 890
    jobId:int
    playerId:int
    
    
