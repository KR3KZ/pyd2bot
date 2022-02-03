from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class JobExperience(NetworkMessage):
    jobId:int
    jobLevel:int
    jobXP:int
    jobXpLevelFloor:int
    jobXpNextLevelFloor:int
    

    def init(self, jobId:int, jobLevel:int, jobXP:int, jobXpLevelFloor:int, jobXpNextLevelFloor:int):
        self.jobId = jobId
        self.jobLevel = jobLevel
        self.jobXP = jobXP
        self.jobXpLevelFloor = jobXpLevelFloor
        self.jobXpNextLevelFloor = jobXpNextLevelFloor
        
        super().__init__()
    
    