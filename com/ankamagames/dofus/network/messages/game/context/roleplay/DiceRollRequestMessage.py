from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DiceRollRequestMessage(NetworkMessage):
    dice:int
    faces:int
    channel:int
    

    def init(self, dice:int, faces:int, channel:int):
        self.dice = dice
        self.faces = faces
        self.channel = channel
        
        super().__init__()
    
    