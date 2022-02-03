from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class FightStartingPositions(NetworkMessage):
    positionsForChallengers:list[int]
    positionsForDefenders:list[int]
    

    def init(self, positionsForChallengers:list[int], positionsForDefenders:list[int]):
        self.positionsForChallengers = positionsForChallengers
        self.positionsForDefenders = positionsForDefenders
        
        super().__init__()
    
    