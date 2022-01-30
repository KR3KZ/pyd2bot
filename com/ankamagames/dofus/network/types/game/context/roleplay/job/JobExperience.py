from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class JobExperience(NetworkMessage):
    protocolId = 1579
    jobId:int
    jobLevel:int
    jobXP:float
    jobXpLevelFloor:float
    jobXpNextLevelFloor:float
    
