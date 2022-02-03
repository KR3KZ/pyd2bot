from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ServerExperienceModificatorMessage(NetworkMessage):
    experiencePercent:int
    

    def init(self, experiencePercent:int):
        self.experiencePercent = experiencePercent
        
        super().__init__()
    
    