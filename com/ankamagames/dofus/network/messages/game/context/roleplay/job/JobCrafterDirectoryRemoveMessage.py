from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class JobCrafterDirectoryRemoveMessage(NetworkMessage):
    protocolId = 890
    jobId:int
    playerId:float
    
