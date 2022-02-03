from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AllianceVersatileInformations(NetworkMessage):
    allianceId:int
    nbGuilds:int
    nbMembers:int
    nbSubarea:int
    

    def init(self, allianceId:int, nbGuilds:int, nbMembers:int, nbSubarea:int):
        self.allianceId = allianceId
        self.nbGuilds = nbGuilds
        self.nbMembers = nbMembers
        self.nbSubarea = nbSubarea
        
        super().__init__()
    
    