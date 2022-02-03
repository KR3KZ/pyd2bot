from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismFightAttackerRemoveMessage(NetworkMessage):
    subAreaId:int
    fightId:int
    fighterToRemoveId:int
    

    def init(self, subAreaId:int, fightId:int, fighterToRemoveId:int):
        self.subAreaId = subAreaId
        self.fightId = fightId
        self.fighterToRemoveId = fighterToRemoveId
        
        super().__init__()
    
    