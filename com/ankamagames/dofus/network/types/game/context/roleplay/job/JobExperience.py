from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class JobExperience(NetworkMessage):
    jobId:int
    jobLevel:int
    jobXP:int
    jobXpLevelFloor:int
    jobXpNextLevelFloor:int
    
    
