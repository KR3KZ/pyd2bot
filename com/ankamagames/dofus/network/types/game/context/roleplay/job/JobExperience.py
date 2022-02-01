from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class JobExperience(INetworkMessage):
    protocolId = 1579
    jobId:int
    jobLevel:int
    jobXP:int
    jobXpLevelFloor:int
    jobXpNextLevelFloor:int
    
    
