from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildInformationsGeneralMessage(NetworkMessage):
    abandonnedPaddock:bool
    level:int
    expLevelFloor:int
    experience:int
    expNextLevelFloor:int
    creationDate:int
    nbTotalMembers:int
    nbConnectedMembers:int
    

    def init(self, abandonnedPaddock:bool, level:int, expLevelFloor:int, experience:int, expNextLevelFloor:int, creationDate:int, nbTotalMembers:int, nbConnectedMembers:int):
        self.abandonnedPaddock = abandonnedPaddock
        self.level = level
        self.expLevelFloor = expLevelFloor
        self.experience = experience
        self.expNextLevelFloor = expNextLevelFloor
        self.creationDate = creationDate
        self.nbTotalMembers = nbTotalMembers
        self.nbConnectedMembers = nbConnectedMembers
        
        super().__init__()
    
    