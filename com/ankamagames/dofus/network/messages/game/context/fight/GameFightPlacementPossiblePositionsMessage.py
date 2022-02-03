from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightPlacementPossiblePositionsMessage(NetworkMessage):
    positionsForChallengers:list[int]
    positionsForDefenders:list[int]
    teamNumber:int
    

    def init(self, positionsForChallengers:list[int], positionsForDefenders:list[int], teamNumber:int):
        self.positionsForChallengers = positionsForChallengers
        self.positionsForDefenders = positionsForDefenders
        self.teamNumber = teamNumber
        
        super().__init__()
    
    